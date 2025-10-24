with open("dog.avif", "rb") as rf:
    with open("dog_copy.avif", "wb") as wf:
        chunk_size = 4096

        chunk = rf.read(chunk_size)
        while len(chunk) > 0:
            wf.write(chunk)
            chunk = rf.read(chunk_size)