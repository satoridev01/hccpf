from hccpf import sendEmail

sendEmail(
    mail_from="sender@example.com",
    mail_to="receiver@example.com",
    mail_subject="Test Email",
    mail_body="This is a test email.",
    smtp_server="smtp.example.com",
    smtp_port=587,
    smtp_user="user",
    smtp_pass="password"
)
