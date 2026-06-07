import streamlit as st
import pdfplumber

from utils.question_generator import generate_questions
from utils.evaluator import evaluate_answer
from utils.report_generator import generate_report
from utils.score_utils import extract_score
from utils.llm_assessment import llm_assessment
from utils.pdf_generator import create_pdf_report
from streamlit_mic_recorder import mic_recorder
from utils.speech_to_text import transcribe_audio
from utils.learning_roadmap import generate_learning_roadmap


st.set_page_config(
    page_title="Interview Session",
    layout="wide"
)

st.title("🎤 AI Interview Session")
######
cv_text = st.session_state.get(
    "cv_text",
    ""
)

job_description = st.session_state.get(
    "job_description",
    ""
)

if not cv_text:

    uploaded_file = st.file_uploader(
        "Upload your CV (PDF)",
        type=["pdf"]
    )

    if uploaded_file is not None:

        text = ""

        with pdfplumber.open(
            uploaded_file
        ) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:

                    text += (
                        page_text
                        + "\n"
                    )

        cv_text = text

        st.session_state[
            "cv_text"
        ] = cv_text

        st.success(
            "✅ CV Uploaded Successfully!"
        )

else:

    st.success(
        "✅ CV Loaded From Main Page"
    )

st.info(
    "Upload your CV and start a real interview simulation."
)

if cv_text:
    
    st.success(
        "✅ CV is Ready"
    )

    st.subheader(
        "CV Preview"
    )

    st.text_area(
        "CV Content",
        cv_text,
        height=300
    )

    if st.button(
        "🚀 Generate Interview Session"
    ):

        with st.spinner(
            "Generating Questions..."
        ):

            questions = generate_questions(
                cv_text,
                job_description
            )

        questions_list = [
            q.strip()
            for q in questions.split("\n")
            if q.strip()
        ]

        st.session_state[
            "session_questions"
        ] = questions_list

        st.session_state[
            "current_question"
        ] = 0

        st.session_state[
            "session_results"
        ] = []
######

    if (
        "session_questions"
        in st.session_state
    ):

        questions = st.session_state[
            "session_questions"
        ]

        current_index = st.session_state[
            "current_question"
        ]

        if current_index < len(questions):

            question = questions[
                current_index
            ]

            st.subheader(
                f"Question {current_index + 1} / {len(questions)}"
            )

            progress = (
                current_index + 1
            ) / len(questions)

            st.progress(
                progress
            )

            st.info(
                question
            )

            answer_mode = st.radio("Choose Answer Method", ["⌨️ Type Answer", "🎤 Voice Answer"], horizontal=True, key=f"mode_{current_index}")

            answer = ""

            if answer_mode == "⌨️ Type Answer":

                 answer = st.text_area("Your Answer", height=200, key=f"answer_{current_index}")

            else:

                st.info("Record your answer using your microphone.")

                audio = mic_recorder(start_prompt="🎤 Start Recording", stop_prompt="⏹ Stop Recording", key=f"recorder_{current_index}")
####
                if audio:

                 with open("temp_audio.wav", "wb") as f:
                    f.write(audio["bytes"])

                 answer = transcribe_audio("temp_audio.wav")

                 st.audio(audio["bytes"])

                 st.success("✅ Voice converted to text")

                 st.text_area("Transcribed Answer", value=answer, height=200, key=f"voice_text_{current_index}")
#####
            col1, col2 = st.columns(2)

            with col1:

                if st.button(
                    "✅ Evaluate Answer"
                ):

                    if answer.strip():

                        with st.spinner(
                            "Evaluating..."
                        ):

                            result = evaluate_answer(
                                question,
                                answer
                            )

                        score = extract_score(
                            result
                        )

                        st.session_state[
                            "last_evaluation"
                        ] = result

                        st.session_state[
                            "last_score"
                        ] = score

                    else:

                        st.warning(
                            "Please enter an answer."
                        )

            if (
                "last_evaluation"
                in st.session_state
            ):

                st.subheader(
                    "📈 Evaluation"
                )

                if (
                    st.session_state[
                        "last_score"
                    ] is not None
                ):

                    st.metric(
                        "Score",
                        f"{st.session_state['last_score']}/10"
                    )

                st.write(
                    st.session_state[
                        "last_evaluation"
                    ]
                )

                with col2:

                    if st.button(
                        "➡️ Next Question"
                    ):

                        st.session_state[
                            "session_results"
                        ].append(
                            {
                                "question":
                                question,

                                "answer":
                                answer,

                                "evaluation":
                                st.session_state[
                                    "last_evaluation"
                                ],

                                "score":
                                st.session_state[
                                    "last_score"
                                ]
                            }
                        )

                        del st.session_state[
                            "last_evaluation"
                        ]

                        del st.session_state[
                            "last_score"
                        ]

                        st.session_state[
                            "current_question"
                        ] += 1

                        st.rerun()

        else:

            st.success(
                "🎉 Interview Session Completed!"
            )

            results = st.session_state[
                "session_results"
            ]

            scores = [
                item["score"]
                for item in results
                if item["score"] is not None
            ]

            average_score = 0
            level = "Needs Improvement"

            if scores:

                average_score = (
                    sum(scores)
                    / len(scores)
                )

                if average_score >= 8:

                    level = "Excellent"

                elif average_score >= 6:

                    level = "Good"

                else:

                    level = (
                        "Needs Improvement"
                    )

                st.subheader(
                    "📊 Interview Statistics"
                )

                col1, col2, col3 = st.columns(3)

                with col1:

                    st.metric(
                        "Questions Answered",
                        len(scores)
                    )

                with col2:

                    st.metric(
                        "Average Score",
                        f"{average_score:.1f}/10"
                    )

                with col3:

                    st.metric(
                        "Performance",
                        level
                    )

            st.subheader(
                "📚 Interview Summary"
            )

            for i, item in enumerate(
                results,
                start=1
            ):

                with st.expander(
                    f"Question {i}"
                ):

                    st.markdown(
                        f"### Score: {item['score']}/10"
                    )

                    st.markdown(
                        "**Question**"
                    )

                    st.write(
                        item["question"]
                    )

                    st.markdown(
                        "**Answer**"
                    )

                    st.write(
                        item["answer"]
                    )

                    st.markdown(
                        "**Evaluation**"
                    )

                    st.write(
                        item["evaluation"]
                    )

            with st.spinner(
                "Generating Final Report..."
            ):

                report = generate_report(
                    results
                )

            st.subheader(
                "📋 Final Interview Report"
            )

            st.write(
                report
            )

            with st.spinner(
                "Generating LLM Assessment..."
            ):

                assessment = llm_assessment(
                    results
                )

            st.subheader(
                "🤖 LLM Interviewer Assessment"
            )

            st.write(
                assessment
            )
            with st.spinner(
                "Generating Learning Roadmap..."
            ):

                roadmap = generate_learning_roadmap(
                    report,
                    assessment
                )

                st.subheader(
                    "🗺️ Learning Roadmap"
                )  

                st.write(
                    roadmap
                )
            statistics_text = f"""
Questions Answered: {len(scores)}

Average Score: {average_score:.1f}/10

Performance: {level}
"""
            
            pdf_file = create_pdf_report(
                statistics_text,
                report,
                assessment,
                roadmap
            )
            st.success("PDF Created : you can download it below!")
            st.write(pdf_file)
            with open(
                pdf_file,
                "rb"
            ) as file:

                st.download_button(
                    label="📄 Download PDF Report",
                    data=file,
                    file_name="Interview_Report.pdf",
                    mime="application/pdf"
                )

