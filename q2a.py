
def output_chuncked_text( txt, length ):
    chunked_lst = []

    ## create length number of chunks
    for i in range(0, length):

        ## iterate through the text line by line, if our index in the txt is the length th position
        ## then add that to the chunk string
        chunk = ''
        for j, char in enumerate(txt):
            if j % length == i:
                chunk += char 
        chunked_lst.append(chunk)

    return chunked_lst

