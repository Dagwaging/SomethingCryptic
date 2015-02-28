from twilio.rest import TwilioRestClient
import web_scraper

account_sid = "AC30d72bd1e9b6f944cf673df52644ac9f"
auth_token = "a0ed6c14de0055bda2c9236a4b6c3c5b"

client = TwilioRestClient(account_sid, auth_token)

def answer(question):
	message = client.messages.get(question.MessageSid)
	question = message.body.split("\n")[-1][:-1]
	answer = web_scraper.scrape(question)
	client.messages.create(body=answer, to="+12172122009", from_="+16147022155")
