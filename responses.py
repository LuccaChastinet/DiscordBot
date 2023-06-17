# File to manage the responses that the bot will give for each message

def handle_response(message) -> str:
    p_message = message.lower() #So he understands the messages if they are $TEST or $test

    if p_message == "$test":
        return "Testando :)"
    
    if p_message == "$oi":
        return "Olá!"
    
    return "Não entendi, desculpe"