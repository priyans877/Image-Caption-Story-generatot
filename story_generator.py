import os
from dotenv import load_dotenv

# Add Azure OpenAI package
from openai import AzureOpenAI


def summary(caption): 
    try: 
    
        # Get configuration settings 
        load_dotenv()
        azure_oai_endpoint ="https://openai0878675.openai.azure.com/"
        azure_oai_key = "2558fb7b74aa49f58474e5a160a99fd3"
        azure_oai_deployment = "gpt-35-turbo-16k"
        
        # Initialize the Azure OpenAI client
        client = AzureOpenAI(
                azure_endpoint = azure_oai_endpoint, 
                api_key=azure_oai_key,  
                api_version="2024-02-15-preview"
                )        

        # Create a system message
        system_message = caption
        print(system_message)
        # Initialize messages array
        messages_array = [{"role": "system", "content": system_message}]
        


                # Get input text
        input_text = caption
        if input_text.lower() == "quit":
            print("No Caption !")
        elif len(input_text) == 0:
            print("Please enter a prompt.")
        
        
        
        print("\nSending request for generating story to Azure OpenAI  ...\n\n")
        
    
        # Add code to send request...
        # Send request to Azure OpenAI model
        # Add code to send request...
        # Send request to Azure OpenAI model
        messages_array.append({"role": "user", "content": input_text})
        
        response = client.chat.completions.create(
            model=azure_oai_deployment,
            temperature=0.7,
            max_tokens=1200,
            messages=messages_array
        )
        generated_text = response.choices[0].message.content
        # Add generated text to messages array
        messages_array.append({"role": "assistant", "content": generated_text})
        
        # Print generated text
        print(f"Story for {caption} \n: " + generated_text + "\n")
            
            
            

    except Exception as ex:
        print(ex)
