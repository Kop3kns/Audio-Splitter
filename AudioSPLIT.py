from pydub import AudioSegment

def process_audio(action, input_files, output_files):
    if action == "split":
        audio = AudioSegment.from_mp3(input_files[0])

        quarter_point = len(audio) // 4
        half_point = len(audio) // 2
        three_quarters_point = 3 * quarter_point

        part1 = audio[:quarter_point]
        part2 = audio[quarter_point:half_point]
        part3 = audio[half_point:three_quarters_point]
        part4 = audio[three_quarters_point:]

        part1.export(output_files[0], format="mp3")
        part2.export(output_files[1], format="mp3")
        part3.export(output_files[2], format="mp3")
        part4.export(output_files[3], format="mp3")
    elif action == "combine":
        audio1 = AudioSegment.from_mp3(input_files[0])
        audio2 = AudioSegment.from_mp3(input_files[1])
        audio3 = AudioSegment.from_mp3(input_files[2])
        audio4 = AudioSegment.from_mp3(input_files[3])

        combined = audio1 + audio2 + audio3 + audio4

        combined.export(output_files[0], format="mp3")
    else:
        print(f"Unknown action {action}. Please use 'split' or 'combine'.")

# Let user choose the action
user_action = input("Enter the action you want to perform (split/combine): ")

if user_action == "split":
    process_audio("split", ["input.mp3"], ["output1.mp3", "output2.mp3", "output3.mp3", "output4.mp3"])
elif user_action == "combine":
    process_audio("combine", ["output1.mp3", "output2.mp3", "output3.mp3", "output4.mp3"], ["combined.mp3"])
else:
    print("Invalid input. Please enter 'split' or 'combine'.")