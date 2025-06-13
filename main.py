import transcriber
import processor
import actions
import json  # <-- Import the json library
from datetime import datetime # <-- Import datetime for unique filenames

# Define the path to your audio file
AUDIO_FILE_PATH = "Special Meeting Audio File - April 29, 2025.mp3" 

def run_pipeline():
    """
    Executes the full meeting assistant pipeline and saves the output.
    """
    # --- Step 1: Transcribe Audio ---
    transcript_text = transcriber.transcribe_audio(AUDIO_FILE_PATH)
    
    if not transcript_text:
        print("Could not get a transcript. Exiting pipeline.")
        return

    print("\n--- TRANSCRIPT ---")
    print(transcript_text)
    print("------------------\n")

    # --- Step 2: Process with Gemini ---
    processed_output = processor.process_transcript_with_gemini(transcript_text)

    if not processed_output:
        print("Could not process the transcript. Exiting pipeline.")
        return
        
    # --- NEW: Step 2.5: Save the processed output to a JSON file ---
    if processed_output:
        # Create a unique filename using a timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"meeting_output_{timestamp}.json"
        
        try:
            with open(output_filename, 'w') as f:
                json.dump(processed_output, f, indent=4) # indent=4 makes it readable
            print(f"\n[SUCCESS] Meeting data saved to {output_filename}")
        except Exception as e:
            print(f"\n[ERROR] Failed to save data to file: {e}")

    # --- Step 3: Display and Execute Actions ---
    print("\n--- MEETING SUMMARY ---")
    print(processed_output.get("summary", "No summary generated."))
    
    print("\n--- MINUTES OF MEETING ---")
    print(processed_output.get("minutes_of_meeting", "No minutes generated."))

    actions.execute_actions(processed_output)

if __name__ == "__main__":
    run_pipeline()