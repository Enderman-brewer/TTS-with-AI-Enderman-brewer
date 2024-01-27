# Settings

This file contains information about the various settings available in the project and how to configure them.

## Adjustable Settings

The following settings can be adjusted to customize the behavior of the project:

**General**

- `delay_after_speech`: The number of seconds to pause after the user stops speaking before responding. (Default: 5)
- `log_file`: The file path where spoken words will be logged. (Default: "word_log.txt")
- `quit_command`: The keyword that triggers the program to quit. (Default: "quit")

**Text-to-Speech (TTS)**

- `voice_index`: The index of the TTS voice to use. (Default: 0)
- `speech_rate`: The speed of the TTS speech in words per minute. (Default: 175)
- `volume`: The overall volume of the TTS output. (Range: 0.0 to 1.0) (Default: 1.0)
- `output_device`: The name of the specific audio output device to use (if applicable). (Default: None)

**Speech-to-Text (STT)**

- `noise_cancellation`: Whether to enable noise cancellation during speech recognition. (Default: True)
- `confidence_threshold`: The minimum confidence level required for recognized text. (Range: 0.0 to 1.0) (Default: 0.5)
- `show_recognized_text`: Whether to display the recognized text on the screen. (Default: True)
- `partial_results`: Whether to report partial results during speaking. (Default: False)

**APIs**

- `chatgpt_api_key`: Your API key for ChatGPT (if applicable). (Default: 0)
- `google_ai_api_key`: Your API key for Google AI (if applicable). (Default: "your_google_ai_api_key")

**Advanced**

- `log_verbosity`: The level of detail to include in logging (1 for basic, 2 for verbose). (Default: 1)
- `api_retries`: The number of times to retry API calls if they fail. (Default: 3)
- `api_timeout`: The timeout in seconds for API calls. (Default: 10)

## How to Change Settings

1. Open the `settings.py` file in a text editor.
2. Locate the setting you want to modify and change its value.
3. Save the `settings.py` file.
4. Restart the program for the changes to take effect.

## Additional Notes

- Some settings may require additional configuration or dependencies. Refer to the documentation for specific details.
- Experiment with different settings to find the best combination for your needs.
