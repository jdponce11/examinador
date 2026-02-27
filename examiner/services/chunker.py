from examiner.models.chunk import Chunk

def divide_book(book, num_pieces):
    chunks: list[Chunk] = []
    book_lenght = len(book.text)
    piece_size = round(book_lenght/num_pieces)
    for num_piece in range(num_pieces):
        lower_piece_index = piece_size*num_piece
        if num_piece == 0:
            start = lower_piece_index
        else:
            start = chunks[num_piece-1].start + chunks[num_piece-1].content.rfind('.') + 1

        if (num_piece+1) == num_pieces:
            new_piece_size = len(book.text) - start
        else:
            new_piece_size = piece_size + book.text[start+piece_size:].find('.')

        content = book.text[start:start+new_piece_size]

        chunk = Chunk(start, content)

        chunks.append(chunk)

    return chunks