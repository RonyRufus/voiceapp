"""Native desktop Voice App using Tkinter (no HTML)."""

from __future__ import annotations

import platform
import shutil
import subprocess
import tkinter as tk
from tkinter import messagebox


class VoiceApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("VoiceApp")
        self.geometry("560x320")
        self.minsize(500, 280)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        title = tk.Label(self, text="VoiceApp (Native)", font=("Arial", 18, "bold"))
        title.grid(row=0, column=0, padx=16, pady=(16, 10), sticky="w")

        self.text_box = tk.Text(self, wrap="word", font=("Arial", 12))
        self.text_box.grid(row=1, column=0, padx=16, pady=8, sticky="nsew")
        self.text_box.insert(
            "1.0",
            "Type text here, then click Speak to use your operating system's built-in speech engine.",
        )

        button_row = tk.Frame(self)
        button_row.grid(row=2, column=0, padx=16, pady=(0, 16), sticky="ew")

        speak_btn = tk.Button(button_row, text="Speak", command=self.speak_text, width=12)
        clear_btn = tk.Button(button_row, text="Clear", command=self.clear_text, width=12)

        speak_btn.pack(side="left")
        clear_btn.pack(side="left", padx=8)

    def clear_text(self) -> None:
        self.text_box.delete("1.0", "end")

    def speak_text(self) -> None:
        text = self.text_box.get("1.0", "end").strip()
        if not text:
            messagebox.showwarning("No text", "Please type something first.")
            return

        system = platform.system().lower()

        try:
            if system == "darwin" and shutil.which("say"):
                subprocess.Popen(["say", text])
                return

            if system == "linux" and shutil.which("espeak"):
                subprocess.Popen(["espeak", text])
                return

            if system == "windows":
                powershell_cmd = (
                    "Add-Type -AssemblyName System.Speech; "
                    "$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; "
                    f"$speak.Speak('{text.replace("'", "''")}')"
                )
                subprocess.Popen(["powershell", "-Command", powershell_cmd])
                return

            messagebox.showinfo(
                "Speech engine unavailable",
                "Could not find a built-in speech command on this machine.\n"
                "Try installing 'espeak' on Linux.",
            )
        except Exception as exc:
            messagebox.showerror("Speech failed", f"Could not speak text.\n\n{exc}")


def main() -> None:
    app = VoiceApp()
    app.mainloop()


if __name__ == "__main__":
    main()
