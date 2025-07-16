# Student Absence Notification System (Python Project)

This project automatically sends **emails and SMS** to parents when a student is marked **absent** in the attendance sheet.

## 🧾 Requirements

- Python 3.x
- Gmail Account (App Password enabled)
- [Twilio Account](https://www.twilio.com/try-twilio) (for SMS)
- `pandas`, `smtplib`, `twilio`

## 📦 Install Dependencies

```bash
pip install pandas twilio
```

## 📝 Edit `attendance.csv`

Update student records with:
```
Name, Date, Status, Email, Phone
```

## 🔐 Set Your Credentials in `config.py`

Replace placeholders with your real email, app password, and Twilio credentials.

## 🚀 Run the Scripts

### Send Absence Emails:
```bash
python send_email.py
```

### Send Absence SMS:
```bash
python send_sms.py
```

✅ Done! Parents will get alerts automatically.
