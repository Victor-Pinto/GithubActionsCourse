import os 

def main():
    name = os.getenv("USERNAME")
    print(f"Welcome {name} ")

if __name__ == "__main__": 
    main()