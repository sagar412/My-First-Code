#Massages program, Chapter 8
msgs = ['I love you Ruchi', 'Biwi chalti kya kone me', 'Biwi you are awesome']
send_msg = []
def send_massages(msgs):
    while msgs:
        sent_msg = msgs.pop()
        print(f"Currently sending: {sent_msg.title()}")
        send_msg.append(sent_msg)

send_massages(msgs[:])
print(msgs)
print(send_msg)
