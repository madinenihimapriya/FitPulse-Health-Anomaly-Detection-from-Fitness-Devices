from preprocess import load_and_preprocess

def main():
    data = load_and_preprocess("data")
    print("Preprocessing completed successfully")
    print(data.head())

if __name__ == "__main__":
    main()
