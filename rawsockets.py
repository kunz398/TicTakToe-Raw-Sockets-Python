import socket
import re
import random
import numpy

#global varibles
SERVER_ADDRESS = (HOST, PORT) = '', 8888
REQUEST_QUEUE_SIZE = 2
history = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'counter': 0}
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#function To decide who wins
def who_wins(x):
        check_X = numpy.array([-1, -1, -1])
        check_O = numpy.array([0, 0, 0])
        # rows and cols
        first_diag = numpy.diag(x)
        second_diag = numpy.diag(numpy.fliplr(x))
        first_col = x[:,0]
        second_col = x[:,1]
        third_col = x[:,2]
        first_row = x[0, :]
        second_row = x[1, :]
        third_row = x[2, :]
        # first Diag
        first_row_count_human = 0
        first_diag_count_human = 0
        second_diag_count_human = 0
        first_col_count_human = 0
        second_col_count_human = 0
        third_col_count_human = 0
        second_row_count_human = 0
        third_row_count_human = 0

        first_diag_count_computer = 0
        second_diag_count_computer = 0
        first_col_count_computer = 0
        second_col_count_computer = 0
        third_col_count_computer = 0
        second_row_count_computer = 0
        third_row_count_computer = 0
        first_row_count_computer = 0

        for i in range(len(second_row)):
            if first_row[i] == check_X[i]:
                first_row_count_human += 1
            if second_row[i] == check_X[i]:
                second_row_count_human += 1
            if third_row[i] == check_X[i]:
                third_row_count_human += 1
            if first_diag[i] == check_X[i]:
                first_diag_count_human += 1
            if second_diag[i] == check_X[i]:
                second_diag_count_human += 1
            if first_col[i] == check_X[i]:
                first_col_count_human += 1
            if second_col[i] == check_X[i]:
                second_col_count_human += 1
            if third_col[i] == check_X[i]:
                third_col_count_human += 1

            if first_row[i] == check_O[i]:
                first_row_count_computer+= 1
            if second_row[i] == check_O[i]:
                second_row_count_computer += 1
            if third_row[i] == check_O[i]:
                third_row_count_computer += 1
            if first_diag[i] == check_O[i]:
                first_diag_count_computer += 1
            if second_diag[i] == check_O[i]:
                second_diag_count_computer += 1
            if first_col[i] == check_O[i]:
                    first_col_count_computer += 1
            if second_col[i] == check_O[i]:
                    second_col_count_computer += 1
            if third_col[i] == check_O[i]:
                    third_col_count_computer += 1

        result = 'The Human Won!'
        if first_row_count_human >= 3:
            fh = open('index.html')
            content = fh.read()
            content = content.replace(re.findall("<h2 id=\"announcer\"></h2>", content)[0],"<h2 id=\"announcer\">" + result + "</h2>")
            fh.close()
            fh = open('index.html', 'w')
            fh.write(content)
        if first_diag_count_human >= 3:
            fh = open('index.html')
            content = fh.read()
            content = content.replace(re.findall("<h2 id=\"announcer\"></h2>", content)[0],"<h2 id=\"announcer\">" + result + "</h2>")
            fh.close()
            fh = open('index.html', 'w')
            fh.write(content)
        if  second_diag_count_human >= 3:
            fh = open('index.html')
            content = fh.read()
            content = content.replace(re.findall("<h2 id=\"announcer\"></h2>", content)[0],"<h2 id=\"announcer\">" + result + "</h2>")
            fh.close()
            fh = open('index.html', 'w')
            fh.write(content)
        if first_col_count_human >= 3:
            fh = open('index.html')
            content = fh.read()
            content = content.replace(re.findall("<h2 id=\"announcer\"></h2>", content)[0],"<h2 id=\"announcer\">" + result + "</h2>")
            fh.close()
            fh = open('index.html', 'w')
            fh.write(content)
        if  second_col_count_human >= 3:
            fh = open('index.html')
            content = fh.read()
            content = content.replace(re.findall("<h2 id=\"announcer\"></h2>", content)[0],"<h2 id=\"announcer\">" + result + "</h2>")
            fh.close()
            fh = open('index.html', 'w')
            fh.write(content)
        if  third_col_count_human >= 3:
            fh = open('index.html')
            content = fh.read()
            content = content.replace(re.findall("<h2 id=\"announcer\"></h2>", content)[0],"<h2 id=\"announcer\">" + result + "</h2>")
            fh.close()
            fh = open('index.html', 'w')
            fh.write(content)
        if  second_row_count_human >= 3:
            fh = open('index.html')
            content = fh.read()
            content = content.replace(re.findall("<h2 id=\"announcer\"></h2>", content)[0],"<h2 id=\"announcer\">" + result + "</h2>")
            fh.close()
            fh = open('index.html', 'w')
            fh.write(content)
        if third_row_count_human >= 3:
            fh = open('index.html')
            content = fh.read()
            content = content.replace(re.findall("<h2 id=\"announcer\"></h2>", content)[0],"<h2 id=\"announcer\">" + result + "</h2>")
            fh.close()
            fh = open('index.html', 'w')
            fh.write(content)

        if first_row_count_computer >= 3:
            result = 'The Computer Won!'
            fh = open('index.html')
            content = fh.read()
            content = content.replace(re.findall("<h2 id=\"announcer\"></h2>", content)[0],
                                  "<h2 id=\"announcer\">" + result + "</h2>")
            fh.close()
            fh = open('index.html', 'w')
            fh.write(content)
        if first_diag_count_computer >= 3:
            result = 'The Computer Won!'
            fh = open('index.html')
            content = fh.read()
            content = content.replace(re.findall("<h2 id=\"announcer\"></h2>", content)[0],
                                  "<h2 id=\"announcer\">" + result + "</h2>")
            fh.close()
            fh = open('index.html', 'w')
            fh.write(content)
        if second_diag_count_computer >= 3:
            result = 'The Computer Won!'
            fh = open('index.html')
            content = fh.read()
            content = content.replace(re.findall("<h2 id=\"announcer\"></h2>", content)[0],
                                  "<h2 id=\"announcer\">" + result + "</h2>")
            fh.close()
            fh = open('index.html', 'w')
            fh.write(content)
        if first_col_count_computer >= 3:
            result = 'The Computer Won!'
            fh = open('index.html')
            content = fh.read()
            content = content.replace(re.findall("<h2 id=\"announcer\"></h2>", content)[0],
                                  "<h2 id=\"announcer\">" + result + "</h2>")
            fh.close()
            fh = open('index.html', 'w')
            fh.write(content)
        if second_col_count_computer >= 3:
            result = 'The Computer Won!'
            fh = open('index.html')
            content = fh.read()
            content = content.replace(re.findall("<h2 id=\"announcer\"></h2>", content)[0],
                                  "<h2 id=\"announcer\">" + result + "</h2>")
            fh.close()
            fh = open('index.html', 'w')
            fh.write(content)
        if third_col_count_computer >= 3:
            result = 'The Computer Won!'
            fh = open('index.html')
            content = fh.read()
            content = content.replace(re.findall("<h2 id=\"announcer\"></h2>", content)[0],
                                  "<h2 id=\"announcer\">" + result + "</h2>")
            fh.close()
            fh = open('index.html', 'w')
            fh.write(content)
        if second_row_count_computer >= 3:
            result = 'The Computer Won!'
            fh = open('index.html')
            content = fh.read()
            content = content.replace(re.findall("<h2 id=\"announcer\"></h2>", content)[0],
                                  "<h2 id=\"announcer\">" + result + "</h2>")
            fh.close()
            fh = open('index.html', 'w')
            fh.write(content)
        if third_row_count_computer >= 3:
            result = 'The Computer Won!'
            fh = open('index.html')
            content = fh.read()
            content = content.replace(re.findall("<h2 id=\"announcer\"></h2>", content)[0],
                                  "<h2 id=\"announcer\">" + result + "</h2>")
            fh.close()
            fh = open('index.html', 'w')
            fh.write(content)

# Function For Reseting the Board
def form_reset(string_list):
    # print 'step:7'
    str1 = str(string_list)
    str2 = str1.find('reset=Reset')
    if str2 == -1:
        return False
    else:
        # print 'step:8'
        history.update({'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'counter': 0})
        global board
        board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        with open('index.html', 'wb+') as output, open('reset.html', 'rb') as input:
            while True:
                data = input.read(100000)  # buffer
                if data == '':
                    break
                output.write(data)
            ### text file
        with open('index.txt', 'wb+') as output, open('reset.txt', 'rb') as input:
            while True:
                data = input.read(100000)  # buffer
                if data == '':
                    break
                output.write(data)

#function for the Humans to make a move
def player_move(players_move, flag):
    flag = False
    if int(players_move) in history.values():
        # print 'step:2'
        move_X = 'X'  # -1
        id = 'position_' + str(players_move)
        history.update({str(players_move): -1})
        history.update({'counter': history.get('counter') + 1})
        for i in range(len(board)):
            for j in range(len(board)):
                if int(players_move) == board[i][j]:
                    board[i][j] = -1



        fh = open('index.html')
        content = fh.read()
        content = content.replace(re.findall("<td id=\"" + id + "\">" + players_move + "</td>", content)[0],
                                  "<td style=\"color:red;\" id=\"" + id + "\">" + move_X + "</td></h2>")
        fh.close()
        fh = open('index.html', 'w')
        fh.write(content)
        flag = True
    else:
        # print 'step:3'
        print "Space is Occupied"
        result = 'The space <span style=\"color:green;\">' + players_move + '</span> is Occupied Try Again!'
        fh = open('index.html')
        content = fh.read()
        content = content.replace(re.findall("<h2 id=\"result\"></h2>", content)[0],
                                  "<h2 id=\"result\">" + result + "</h2>")
        fh.close()
        fh = open('index.html', 'w')
        fh.write(content)
        flag = False

    return flag

#function for the computer to make a move
def computers_turn(flag):
    computer_move = random.randint(1, 9)
    print 'Computer Move: ' + str(computer_move)
    if int(computer_move) in history.values():
        # print 'step:5'
        # print 'Computer Move: ' + str(computer_move)
        move_O = 'O'
        history.update({str(computer_move): 0})
        history.update({'counter': history.get('counter') + 1})
        for i in range(len(board)):
            for j in range(len(board)):
                if int(computer_move) == board[i][j]:
                    board[i][j] = 0
        fh = open('index.html')
        content = fh.read()
        id = 'position_' + str(computer_move)
        content = content.replace(re.findall("<td id=\"" + id + "\">" + str(computer_move) + "</td>", content)[0],
                                  "<td style=\"color:blue;\" id=\"" + id + "\">" + move_O + "</h2>")
        fh = open('index.html', 'w')
        fh.write(content)
        fh.close()
        flag = False
    else:
        if history.get('counter') >= 9:  # end of game
            # print 'step:6'
            flag = False
        else:
            # print 'step:6.1'
            flag = True
    return flag

#functions fr calculating all the submissions and condiions
def cal(string_list, position_value_, flag):  # Function For Placing Cross And Noughts
    try:
        if (form_submit(string_list)):
            # Players moves
            # print 'step:1'
            flag = player_move(position_value_, flag)
            # Players moves

            # computer moves
            while flag:
                # print 'step:4'
                flag = computers_turn(flag)
                # computer moves

        # check if any one won#
        winner = 0 # unknown state || -1 computer win || 1 player win
        dict_1 = history.copy()
        del dict_1['counter']
        # convert to 2D array
        l = [x for x in dict_1.values()]
        l.sort()
        step = 3
        mat = ([x for x in [l[start:start + step] for start in range(0, len(l), step)]])
        x = numpy.array(board)
        print numpy.matrix(board)
        ##########
        who_wins(x)


    except Exception as e:
        print 'Exception101: ' + str(e)
        form_reset(string_list)

#function for handling submiissions
def form_submit(string_list):
    str1 = str(string_list)
    str2 = str1.find('submit=Submit')
    if str2 == -1:
        return False
    else:
        return True

# Function For Fetching the Position of the Inserted Data
def form_pos_value(string_list):

    if len(string_list) > 26:
        try:
            form_data = string_list[29]
            form_data = form_data.split('\n')
            form_data_parsed = form_data[2]
            form_data_parsed = form_data_parsed.split('&')
            form_data_position = form_data_parsed[0]
            form_data_position = form_data_position.split('=')
            position_value_ = form_data_position[1]
        except:
            position_value_ = ''
    else:
        position_value_ = ''
    print position_value_
    return position_value_

# Function For Handling Request
def handle_request(client_connection):
    request = client_connection.recv(1024)

    string_list = request.split(' ')
    position_value = form_pos_value(string_list)
    form_reset(string_list)  # reset_form

    print 'Player Move: ' + position_value
    flag = False
    cal(string_list, position_value, flag)

    try:
        requesting_file = string_list[1]
        myfile = requesting_file.split('?')[0]

        myfile = myfile.lstrip('/')
    except:
        myfile = 'index.html'

    if ((myfile == '/index.html') or (myfile == '') or (myfile == '/')):
        myfile = 'index.html'
    try:
        file = open(myfile, 'rb')
        response = file.read()
        file.close()

        header = 'HTTP/1.1 200 OK\n'

        if (myfile.endswith(".jpg")):
            mimetype = 'image/jpg'
        elif (myfile.endswith(".css")):
            mimetype = 'text/css'
        else:
            mimetype = 'text/html'

        header += 'Content-Type: ' + str(mimetype) + '\n\n'

    except Exception as e:
        header = 'HTTP/1.1 404 Not Found\n\n'
        response = '<html><body><center><h3>Error 404: File not found</h3><p>Python HTTP Server</p></center></body></html>'.encode(
            'utf-8')
    final_response = header.encode('utf-8')
    final_response += response
    client_connection.sendall(final_response)

#basic server code
def serve_forever():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind(SERVER_ADDRESS)
    listen_socket.listen(REQUEST_QUEUE_SIZE)

    print('Serving HTTP on port {port} ...'.format(port=PORT))

    while True:
        client_connection, client_address = listen_socket.accept()
        handle_request(client_connection)
        client_connection.close()

serve_forever() #main program
