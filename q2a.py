
def output_chuncked_text( txt, length ):
    chunked_lst = []

    for i in range(0, length):

        chunk = ''
        for j, char in enumerate(txt):
            if j % length == i:
                chunk += char 
        chunked_lst.append(chunk)

    return chunked_lst

