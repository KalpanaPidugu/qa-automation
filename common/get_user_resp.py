



def get_user_response_text(msg):
    resp = input(f"{msg}\n")
    return resp

def get_user_response_yn(msg) -> bool:
    resp = input(f"{msg} ? Type 'Y' or 'N' \n")
    resp = True if resp.lower() == 'y' else False
    return resp