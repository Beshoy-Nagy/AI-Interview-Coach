\# AI Interview Coach



AI Interview Coach is an AI-powered platform that helps candidates analyze their CVs, prepare for interviews, improve ATS scores, generate tailored cover letters, and receive personalized career guidance.



\## Features



\### CV Analysis



\* Extracts text from PDF resumes.

\* Analyzes strengths, weaknesses, and improvement opportunities.



\### Job Description Matching



\* Compares the candidate's CV against a target job description.

\* Provides a detailed recruiter-style assessment.

\* Generates a match score and improvement recommendations.



\### ATS Score Analysis



\* Calculates an ATS compatibility score.

\* Identifies matched keywords.

\* Highlights missing keywords and skills.



\### AI Resume Rewriter



\* Rewrites and optimizes the CV for a specific job description.

\* Improves ATS compatibility.

\* Preserves factual information without inventing experience.



\### Cover Letter Generator



\* Generates customized cover letters based on the candidate's CV and job requirements.

\* Highlights relevant skills and projects.



\### AI Interview Question Generator



\* Generates technical and behavioral interview questions based on:



&#x20; \* Candidate CV

&#x20; \* Target Job Description



\### Interview Session



\* Interactive interview experience.

\* Supports both:



&#x20; \* Text Answers

&#x20; \* Voice Answers



\### Voice-to-Text Transcription



\* Converts recorded answers into text using Whisper.



\### AI Answer Evaluation



\* Evaluates interview answers.

\* Provides feedback and scoring.



\### Interview Analytics Dashboard



\* Visualizes interview performance.

\* Displays:



&#x20; \* Performance trend

&#x20; \* Highest score

&#x20; \* Lowest score

&#x20; \* Average score



\### AI Interview Insights



\* Identifies:



&#x20; \* Strengths

&#x20; \* Weaknesses

&#x20; \* Skills to improve

&#x20; \* Final recommendations



\### Learning Roadmap



\* Generates a personalized learning plan based on interview performance.



\### Final Interview Report



\* Creates a complete interview assessment report.

\* Exportable as PDF.



\---



\## Tech Stack



\### Frontend



\* Streamlit



\### AI \& Machine Learning



\* Ollama

\* Qwen 3

\* Whisper



\### Data Processing



\* Pandas

\* NumPy

\* PDFPlumber



\### Visualization



\* Matplotlib



\### Reporting



\* ReportLab



\---



\## Project Structure



```text

AI-Interview-Coach/

│

├── pages/

│   └── 1\_Interview\_Session.py

│

├── utils/

│   ├── ats\_score.py

│   ├── cover\_letter.py

│   ├── cv\_analyzer.py

│   ├── cv\_rewriter.py

│   ├── evaluator.py

│   ├── interview\_analytics.py

│   ├── job\_matcher.py

│   ├── learning\_roadmap.py

│   ├── ollama\_client.py

│   ├── question\_generator.py

│   ├── report\_generator.py

│   └── ...

│

├── ScreenShots/

├── cv\_readerApp.py

├── requirements.txt

└── README.md

```



\---



\## Installation



\### Clone Repository



```bash

git clone https://github.com/YOUR\_USERNAME/AI-Interview-Coach.git



cd AI-Interview-Coach

```



\### Install Dependencies



```bash

pip install -r requirements.txt

```



\### Install Ollama



Download and install Ollama:



https://ollama.com



Pull the required model:



```bash

ollama pull qwen3:4b

```



\### Run Application



```bash

streamlit run cv\_readerApp.py

```



\---



\## Future Improvements



\* RAG-based Resume Analysis

\* Vector Database Integration

\* Multi-LLM Support

\* Interview Video Analysis

\* Online Deployment

\* Authentication System



\---



\## Author



Beshoy Nagy



AI Engineer



Benha University – Faculty of Computers and Artificial Intelligence



