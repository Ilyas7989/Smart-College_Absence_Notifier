import pandas as pd
import smtplib
from email.mime.text import MIMEText
from config import GMAIL_USER, GMAIL_PASS

def send_absence_emails():
    df = pd.read_csv("attendance.csv")

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(GMAIL_USER, GMAIL_PASS)

    for _, row in df.iterrows():
        if row["Status"].lower() == "absent":
            msg = MIMEText(
                f"Dear Parent,\n\n"
                f"This is to inform you that {row['Name']} was absent on {row['Date']}.\n"
                f"If you have any concerns, please contact the college administration.\n\n"
                f"Regards,\nCollege Admin"
            )
            msg["Subject"] = "College Absence Notification"
            msg["From"] = GMAIL_USER
            msg["To"] = row["Email"]

            server.sendmail(GMAIL_USER, row["Email"], msg.as_string())
            print(f"📧 Email sent to {row['Name']}'s parent ({row['Email']}) | 📞 Phone: {row['Phone']}")

    server.quit()
    print("✅ All absence emails sent successfully.")

if __name__ == "__main__":
    send_absence_emails()
