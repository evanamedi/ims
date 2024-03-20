# import logging
# from database.db_utils import db_cursor
# from database.db_show import show_database
# from add_or_update import add_update

# logging.basicConfig(filename= "main.log", filemode= "w", format= "%(asctime)s | %(name)s | %(levelname)s | %(message)s")
# logger = logging.getLogger(__name__)

# # Constant for user commands
# CMD_SHOW_DATABASE = 1
# CMD_ADD_UPDATE = 2
# CMD_EXIT = 0

        

    
# def main():
#     try:
#         with db_cursor() as cursor:
#             cursor.execute("SELECT DATABASE();")
#             result = cursor.fetchone()
#             print()
#             print("Welcome...")
#             print("Connected to database: ", result[0])

#         while True:
#             try:
#                 command = int(input("\n--------------------Main Menu--------------------\n"
#                                     f"{CMD_SHOW_DATABASE} for table names\n"
#                                     f"{CMD_ADD_UPDATE} to add/update\n"
#                                     f"{CMD_EXIT} to end \n"))
#             except ValueError:
#                 print("Invalid input. Please enter a number.")
#                 logger.warning("Invalid Input. Value outside constraints")
#                 continue

#             if command == CMD_EXIT:
#                 break
#             elif command == CMD_SHOW_DATABASE:
#                 print()
#                 print(show_database())
#             elif command == CMD_ADD_UPDATE:
#                 add_update()
#             else:
#                 print("Invalid input")
#     except KeyboardInterrupt:
#         print("\n\nOhhh no i've been terminated...")
#         logger.warning("Program Terminated")
#     finally:
#         print("\nFarewell comrade")


# if __name__ == "__main__":
#     main()