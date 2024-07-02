import requests
import json


def summarize_using_llama3(chunk):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "llama3",
        "prompt": "This is a meeting. Summarize this and Generate meeting meeting minutes from this. \n: " + chunk,
        "stream": False,
    }

    headers = {"Content-Type": "application/json"}

    response = requests.post(url, data=json.dumps(payload), headers=headers)

    # Parse the JSON response
    response_data = response.json()

    # Extract and print the "response" field
    return response_data["response"]


def chunk_text(text, chunk_size=1000):
    words = text.split()
    total_chunks = (
        len(words) + chunk_size - 1
    ) // chunk_size  # Calculate the total number of chunks
    for i in range(total_chunks):
        yield " ".join(words[i * chunk_size : (i + 1) * chunk_size])


def process_chunks(file_path, chunk_size=1000):
    with open(file_path, "r") as file:
        text = file.read()

    summarized_chunks = []
    
    word_count = len(text)
    # print("word count: ", word_count)

    if word_count > 5000:
        for chunk in chunk_text(text, chunk_size):
            sum_chunk = summarize_using_llama3(chunk)
            sum_chunk += "\n"
            summarized_chunks.append(sum_chunk)
    else:
        sum_chunk = summarize_using_llama3(text)
        sum_chunk += "\n"
        summarized_chunks.append(sum_chunk)

    return summarized_chunks


# Example usage
file_path = "test.txt"
summarized_chunk_arr = process_chunks(file_path)

# # Print summarized chunks to verify
# #  TOOD if chunk size >= 2, summarize further...
# for i, summarized_chunk in enumerate(summarized_chunk_arr):
#     print(f"Chunk {i+1}: {summarized_chunk}")

combined_summary = " ".join(summarized_chunk_arr)

sum_chunk = summarize_using_llama3(combined_summary)
print(sum_chunk)
