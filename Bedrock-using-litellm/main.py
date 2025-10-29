from litellm import completion
import litellm
litellm.callbacks = ["otel"]

from dotenv import load_dotenv
load_dotenv()

from traceloop.sdk import Traceloop
Traceloop.init(app_name="LitellmApp")

# Example: Using Amazon Titan Text Express on Bedrock
response = completion(
    model="bedrock/amazon.titan-text-express-v1",
    messages=[
        {"role": "system", "content": "You are an assistant that summarizes text."},
        {"role": "user", "content": "Summarize this: Large language models are transforming the way software is built."},
    ],
)

print("Response from Bedrock model:")
print(response['choices'][0]['message']['content'])