import aiassist

question1 = "Who won the world series in 2020?"
req = aiassist.Completion.create(prompt=question1)
answer = req["text"]
message_id = req["parentMessageId"]

question2 = "Where was it played?"
req2 = aiassist.Completion.create(prompt=question2, parentMessageId='chatcmpl-7R6TJeFwGuy1gpGerrehNQ2UKQcWX')
answer2 = req2["text"]

print(answer)
print(answer2)