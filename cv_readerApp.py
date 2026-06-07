import streamlit as st
import pdfplumber
import pandas as pd
import matplotlib.pyplot as plt
from utils.cv_analyzer import analyze_cv
from utils.question_generator import generate_questions
from utils.evaluator import evaluate_answer
from utils.report_generator import generate_report
from utils.score_utils import extract_score
from utils.job_matcher import match_cv_to_job
from utils.ats_score import calculate_ats_score 
from utils.cv_rewriter import rewrite_cv
from utils.cover_letter import generate_cover_letter
from utils.interview_analytics import analyze_interview

st.set_page_config(
    page_title="AI Interview Coach",
    layout="wide"
)

st.title(" AI Interview Coach")


uploaded_file = st.file_uploader(
    "Upload your CV (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:

    text = ""

    with pdfplumber.open(uploaded_file) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    st.success("✅ CV Uploaded Successfully!")

    job_description = st.text_area(
        "Paste Job Description",
        height=250,
        placeholder="Paste the job description here..."
    )

    with st.expander("View Extracted CV Text"):

        st.text_area(
            "CV Content",
            text,
            height=300
        )
    #####
    
    col1, col2, col3, col4, col5,col6 = st.columns(6)

    # Analyze CV
    with col1:

        if st.button("📄 Analyze CV"):

            with st.spinner("Analyzing CV..."):

                analysis = analyze_cv(text)

            st.session_state["analysis"] = analysis

    # Generate Questions
    with col2:

        if st.button("🎯 Generate Interview Questions"):

            with st.spinner("Generating Questions..."):

                questions = generate_questions(
                    text, 
                    job_description
                    )

            st.session_state["questions"] = questions
    # Interview Session       
    with col3:

        if st.button(
            "🎤 Start Interview Session"
        ):

            st.session_state[
                "cv_text"
            ] = text

            st.session_state[
                "job_description"
            ] = job_description

            st.switch_page(
                "pages/1_Interview_Session.py"
            )
    #Job Decription Matching
    with col4:

        if st.button("🔍 Match CV to Job Description"):

            if not job_description.strip():

                st.warning(
                    "Please enter a job description first."
                )

            else:

                with st.spinner(
                    "Matching CV to Job Description..."
                ):

                    match_result = match_cv_to_job(
                        text,
                        job_description
                    )

                st.session_state[
                    "match_result"
                ] = match_result
                
                ats_result = calculate_ats_score(
                    text,
                    job_description
                )

                st.session_state[
                    "ats_result"
                ] = ats_result
                
                st.session_state[
                    "original_ats_score"
                ] = ats_result["score"]
                
    # Rewrite CV          
    with col5:

        if st.button(
            "✨ Improve CV"
        ):

            if not job_description.strip():

                st.warning(
                    "Please enter a job description first."
                )

            else:

                with st.spinner(
                    "Improving CV..."
                ):

                    if (
                        "original_ats_score"
                        not in st.session_state
                    ):

                        original_ats = (
                            calculate_ats_score(
                                text,
                                job_description
                            )
                        )

                        st.session_state[
                            "original_ats_score"
                        ] = original_ats[
                            "score"
                        ]

                    result = rewrite_cv(
                        text,
                        job_description
                    )

                    improved_ats = (
                        calculate_ats_score(
                            result,
                            job_description
                        )
                    )

                st.session_state[
                    "cv_rewrite"
                ] = result

                st.session_state[
                    "improved_ats"
                ] = improved_ats
    # Generate Cover Letter
    with col6:

        if st.button(
            "✉️ Generate Cover Letter"
        ):

            if not job_description.strip():

                st.warning(
                    "Please enter a job description first."
                )

            else:

                with st.spinner(
                    "Generating Cover Letter..."
                ):

                    cover_letter = (
                        generate_cover_letter(
                            text,
                            job_description
                        )
                    )

                st.session_state[
                    "cover_letter"
                ] = cover_letter                  
                
    # Show Analysis
    if "analysis" in st.session_state:

        st.subheader("📊 CV Analysis")

        st.write(
            st.session_state["analysis"]
        )
        # Show Job Match Result
    if "match_result" in st.session_state:

        st.subheader("🔍 CV to Job Match Result")

        st.write(
            st.session_state[
                "match_result"
            ]
        )
    # Show ATS Score
    if "ats_result" in st.session_state:

        ats = st.session_state[
            "ats_result"
        ]

        st.subheader(
            "📊 ATS Score"
        )

        st.metric(
            "ATS Score",
            f"{ats['score']}%"
        )

        col1, col2 = st.columns(2)

        with col1:

            st.markdown(
                "### ✅ Matched Keywords"
            )

            st.write(
                ats["matched"]
            )

        with col2:

            st.markdown(
                "### ❌ Missing Keywords"
            )

            st.write(
                ats["missing"]
            )  
    
        #show cover letter
    if "cover_letter" in st.session_state:

        st.subheader(
            "📄 Cover Letter"
        )

        st.markdown(
            st.session_state[
                "cover_letter"
            ]
        )

        st.download_button(
            "⬇️ Download Cover Letter",
            st.session_state[
                "cover_letter"
            ],
            file_name="cover_letter.txt"
        )  
    #show cv rewrite
    if "cv_rewrite" in st.session_state:

        st.subheader(
            "✨ Improved CV"
        )

        st.markdown(
            st.session_state[
                "cv_rewrite"
            ]
        )

        st.download_button(
            "⬇️ Download Improved CV",
            st.session_state[
                "cv_rewrite"
            ],
            file_name="improved_cv.txt"
        )
        
        if (
            "original_ats_score"
            in st.session_state
            and
            "improved_ats"
            in st.session_state
        ):

            before_score = (
                st.session_state[
                "original_ats_score"
                ]
            )

            after_score = (
                st.session_state[
                    "improved_ats"
                ]["score"]
            )

            improvement = (
                after_score
                -
                before_score
            )

            st.subheader(
                "📈 ATS Improvement"
            )

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "ATS Before",
                    f"{before_score}%"
                )

            with col2:

                st.metric(
                    "ATS After",
                    f"{after_score}%"
                )

            with col3:

                st.metric(
                    "Improvement",
                    f"+{improvement}%"
                )
              
    # Show Questions
    if "questions" in st.session_state:

        st.subheader("📝 Interview Questions")

        questions_text = st.session_state["questions"]

        questions = [
            q.strip()
            for q in questions_text.split("\n")
            if q.strip()
        ]

        selected_question = st.selectbox(
            "Choose a Question",
            questions
        )

        st.markdown("### Selected Question")

        st.info(selected_question)

        answer = st.text_area(
            "Your Answer",
            height=200,
            placeholder="Type your answer here..."
        )

        if st.button("✅ Evaluate Answer"):

            if not answer.strip():

                st.warning(
                    "Please enter an answer first."
                )

            else:

                with st.spinner(
                    "Evaluating Answer..."
                ):

                    result = evaluate_answer(
                        selected_question,
                        answer
                    )

                if (
                    "evaluations"
                    not in st.session_state
                ):

                    st.session_state[
                        "evaluations"
                    ] = []

                st.session_state[
                    "evaluations"
                ].append(
                    {
                        "question":
                        selected_question,

                        "answer":
                        answer,

                        "evaluation":
                        result
                    }
                )

                st.subheader(
                    "📈 Evaluation Result"
                )

                st.write(result)
    # Interview Session

    if st.session_state.get(
         "interview_mode",
         False
        ):

         st.divider()

         st.header("🎤 Interview Session")
        
         

         st.info("Interview Session Started")
        
        
    # Interview History
    if "evaluations" in st.session_state:

        st.subheader("📚 Interview History")

        st.write(
            f"Questions Answered: {len(st.session_state['evaluations'])}"
        )

        for i, item in enumerate(
            st.session_state["evaluations"],
            start=1
        ):

            with st.expander(
                f"Question {i}"
            ):

                st.markdown(
                    "### Question"
                )

                st.write(
                    item["question"]
                )

                st.markdown(
                    "### Your Answer"
                )

                st.write(
                    item["answer"]
                )

                st.markdown(
                    "### Evaluation"
                )

                st.write(
                    item["evaluation"]
                )

        st.divider()

        # Generate Report Button
        if st.button(
            "📄 Generate Final Report"
        ):

            with st.spinner(
                "Generating Report..."
            ):

                report = generate_report(
                    st.session_state[
                        "evaluations"
                    ]
                )

            st.session_state[
                "final_report"
            ] = report
    

# Interview Statistics

if "evaluations" in st.session_state:

    scores = []

    for item in st.session_state["evaluations"]:

        score = extract_score(
            item["evaluation"]
        )

        if score is not None:

            scores.append(score)

    if scores:

        average_score = (
            sum(scores) / len(scores)
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

            if average_score >= 8:

                level = "Excellent"

            elif average_score >= 6:

                level = "Good"

            else:

                level = "Needs Improvement"

            st.metric(
                "Performance",
                level
            )
            ##############
    # Interview Analytics Dashboard    
        st.subheader(
            "📊 Interview Analytics Dashboard"
        )

        scores_df = pd.DataFrame(
            {
                "Question":
                list(
                    range(
                        1,
                        len(scores) + 1
                    )
                ),

                "Score":
                scores
            }
        )

        fig, ax = plt.subplots()

        ax.plot(
            scores_df["Question"],
            scores_df["Score"],
            marker="o"
        )

        ax.set_title(
            "Interview Performance Trend"
        )

        ax.set_xlabel(
            "Question Number"
        )

        ax.set_ylabel(
            "Score"
        )

        st.pyplot(fig)

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Highest Score",
                max(scores)
            )

        with col2:

            st.metric(
                "Lowest Score",
                min(scores)
            )

        with col3:

            st.metric(
                "Score Range",
                max(scores) - min(scores)
            )
            ##############
    if st.button(
        "📈 Analyze Interview Performance"
    ):

        with st.spinner(
            "Analyzing..."
        ):

            analytics = (
                analyze_interview(
                    st.session_state[
                        "evaluations"
                    ]
                )
            )

        st.session_state[
            "analytics"
        ] = analytics      
    if "analytics" in st.session_state:

        st.subheader(
            "🧠 AI Interview Insights"
        )

        st.write(
            st.session_state[
                "analytics"
            ]
        )      
    # Show Final Report
    if "final_report" in st.session_state:

        st.subheader(
            "📋 Final Interview Report"
        )

        st.write(
            st.session_state[
                "final_report"
            ]
        )