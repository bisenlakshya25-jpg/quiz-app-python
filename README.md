# 🧠 Quiz App (Python)

A command-line Quiz Application built using Python. The application allows users to play quizzes from different categories and difficulty levels with random question selection, score calculation, accuracy tracking, and detailed performance feedback.

---

## ✨ Features

- Multiple Quiz Categories
- Multiple Difficulty Levels
- Random Question Selection
- User-selectable Number of Questions
- Input Validation
- Skip Questions using `Q`
- Configurable Marking Scheme
- Negative Marking Support
- Accuracy Calculation
- Review Correct Answers after Quiz
- JSON-based Question Database
- Clean and Modular Code

---

## 📂 Project Structure

```
Quiz-App/
│
├── main.py
├── questions.json
├── README.md
```

---

## 📄 Question Database Format

Questions are stored inside a JSON file.

Example:

```json
{
    "Python": {
        "Easy": {
            "marking": {
                "correct": 1,
                "wrong": 0
            },
            "questions": {
                "1": {
                    "question": "...",
                    "options": {
                        "1": "...",
                        "2": "...",
                        "3": "...",
                        "4": "..."
                    },
                    "answer": "2"
                }
            }
        }
    }
}
```

---

## 🎮 How to Play

1. Start the application.
2. Select a quiz category.
3. Choose the difficulty level.
4. Select the number of questions.
5. Answer using option numbers (1–4).
6. Press `Q` to skip any question.
7. View your final score, accuracy, and correct answers.

---

## 📊 Result Summary

After completing the quiz, the application displays:

- Final Score
- Total Questions
- Correct Answers
- Wrong Answers
- Skipped Questions
- Accuracy Percentage
- Performance Feedback
- Correct Answers for Wrong/Skipped Questions

---

## 🛠️ Technologies Used

- Python
- JSON
- Random Module
- File Handling

---

## 🚀 Future Improvements

- Timer for Each Question
- Player Name & Score History
- Leaderboard
- Add Questions from the Application
- Shuffle Answer Options
- Question Statistics
- GUI Version

---

## 👨‍💻 Author

Lakshya