import assemblyai as aai
from config import ASSEMBLYAI_API_KEY

def transcribe_audio(file_path: str) -> str:
    """
    Transcribes an audio file with speaker diarization using AssemblyAI.

    Args:
        file_path (str): The path to the local audio file.

    Returns:
        str: A formatted string of the transcript with speaker labels.
    """
    print("Starting transcription...")
    
    # Set the API key
    aai.settings.api_key = ASSEMBLYAI_API_KEY

    # Configure the transcription options
    config = aai.TranscriptionConfig(speaker_labels=True)

    # Create a transcriber object
    transcriber = aai.Transcriber()

    # Perform the transcription
    try:
        transcript = transcriber.transcribe(file_path, config)
    except Exception as e:
        print(f"Error during transcription: {e}")
        return None

    if transcript.status == aai.TranscriptStatus.error:
        print(f"Transcription failed: {transcript.error}")
        return None

    # Format the output
    formatted_transcript = []
    if transcript.utterances:
        for utterance in transcript.utterances:
            formatted_transcript.append(f"Speaker {utterance.speaker}: {utterance.text}")
    else:
        # Fallback if no utterances are found (e.g., for non-diarized short audio)
        return transcript.text

    print("Transcription finished successfully.")
    return "\n".join(formatted_transcript)