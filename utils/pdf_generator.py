from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def create_pdf_report(
    statistics,
    report,
    assessment,
    roadmap
):

    pdf_file = "interview_report.pdf"

    doc = SimpleDocTemplate(
        pdf_file
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "AI Interview Coach Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            "Interview Statistics",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            statistics,
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            "Final Interview Report",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            report,
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            "LLM Assessment",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            assessment,
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            "Learning Roadmap",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            roadmap,
            styles["BodyText"]
        )
    )

    doc.build(content)

    return pdf_file