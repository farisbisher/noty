class AuthChecker():

    def get_auth_data(self):
        try:
            file = open("auth_data.txt", 'r')
            for line in file:
                content = line.split(',')
            
            token = content[0]
            database_id = content[1]


        except FileNotFoundError:
            token = input('Insert your Notion auth token: ')
            database_id = input('Insert your Notion database Id: ')

            file = open("auth_data.txt", "w")
            file.write(f"{token},{database_id}")

        return token, database_id






