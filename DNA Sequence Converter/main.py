print("#===Welcome to DNA/mRNA/tRNA/Anino Acid (Protein) Sequence Converter===#")
start = input("Press Enter to continue...")
while True:
    if start == "":
        print("Check Available Options:")
        print("1. DNA")
        print("2. mRNA")
        print("3. tRNA")
        print("4. Amino Acid(Protein)")
        print("")
        command = (input("Select input option(1-4): "))

        if command == "1":
            print("1. mRNA")
            print("2. tRNA")
            command2 = (input("Select output option(1,2): "))
            data = input("Enter the DNA sequence: ")
            result = ""
            if command2 == "1":
                for x in data:
                    if x.upper() == "A":
                        result += "A"
                    elif x.upper() == "T":
                        result += "U"
                    elif x.upper() == "C":
                        result += "C"
                    elif x.upper() == "G":
                        result += "G"
            elif command2 == "2":
                for x in data:
                    if x.upper() == "A":
                        result += "U"
                    elif x.upper() == "T":
                        result += "A"
                    elif x.upper() == "C":
                        result += "G"
                    elif x.upper() == "G":
                        result += "C"
            else: print("Invalid Command")
            print(result)
        elif command == "2":
            print("1. DNA")
            print("2. tRNA")
            command2 = (input("Select output option(1,2): "))
            data = input("Enter the mRNA sequence: ")
            result = ""
            if command2 == "1":
                for x in data:
                    if x.upper() == "A":
                        result += "A"
                    elif x.upper() == "T":
                        result += "U"
                    elif x.upper() == "C":
                        result += "C"
                    elif x.upper() == "G":
                        result += "G"
            elif command2 == "2":
                for x in data:
                    if x.upper() == "A":
                        result += "U"
                    elif x.upper() == "U":
                        result += "A"
                    elif x.upper() == "C":
                        result += "G"
                    elif x.upper() == "G":
                        result += "C"
                print(result)
            else: print("Invalid Command")
        elif command == "3":
            print("1. DNA")
            print("2. mRNA")
            command2 = (input("Select output option(1,2): "))
            data = input("Enter the tRNA sequence: ")
            result = ""
            if command2 == "1":
                for x in data:
                    if x.upper() == "A":
                        result += "T"
                    elif x.upper() == "U":
                        result += "A"
                    elif x.upper() == "C":
                        result += "G"
                    elif x.upper() == "G":
                        result += "C"
                print(result)
            elif command2 == "2":
                for x in data:
                    if x.upper() == "A":
                        result += "U"
                    elif x.upper() == "U":
                        result += "A"
                    elif x.upper() == "C":
                        result += "G"
                    elif x.upper() == "G":
                        result += "C"
                print(result)
            elif command2 == "3":
                print(data)
            else: print("Invalid Command")
        elif command == "4":
            data = input("Enter mRNA sequence: ")
            result = ""
            array = []
            if len(data)%3 != 0:
                print("Invalid Sequence")
            else:
                for x in range(len(array)):
                    if array[x] == "UUU" or array[x] == "UUC":
                        result += "Phe"+"-"
                    elif array[x] == "UUA" or array[x] == "UUG" or array[x] == "CUU" or array[x] == "CUC" or array[x] == "CUA" or array[x] == "CUG":
                        result += "Leu"+"-"
                    elif array[x] == "UCU" or array[x] == "UCC" or array[x] == "UCA" or array[x] == "UCG" or array[x] == "AGU" or array[x] == "AGC":
                        result += "Ser"+"-"
                    elif array[x] == "UAU" or array[x] == "UAC":
                        result += "Tyr"+"-"
                    elif array[x] == "UGU" or array[x] == "UGC":
                        result += "Cys"+"-"
                    elif array[x] == "CCU" or array[x] == "CCC" or array[x] == "CCA" or array[x] == "CAG":
                        result += "Pro"+"-"
                    elif array[x] == "CAU" or array[x] == "CAC":
                        result += "His"+"-"
                    elif array[x] == "CAA" or array[x] == "CAG":
                        result += "Gin"+"-"
                    elif array[x] == "CGU" or array[x] == "CGC" or array[x] == "CGA" or array[x] == "CGG" or array[x] == "AGA" or array[x] == "AGG":
                        result += "Arg"+"-"
                    elif array[x] == "UGG":
                        result += "Trp"+"-"
                    elif array[x] == "AUG":
                        result += "Met"+"-"
                    elif array[x] == "AUU" or array[x] == "AUC" or array[x] == "AUA":
                        result += "Ile"+"-"
                    elif array[x] == "ACU" or array[x] == "ACC" or array[x] == "ACA" or array[x] == "ACG":
                        result += "Thr"+"-"
                    elif array[x] == "AAU" or array[x] == "AAC":
                        result += "Asn"+"-"
                    elif array[x] == "AAA" or array[x] == "AAG":
                        result += "Lys"+"-"
                    elif array[x] == "GUU" or array[x] == "GUC" or array[x] == "GUA" or array[x] == "GUG":
                        result += "Val"+"-"
                    elif array[x] == "GCU" or array[x] == "GCC" or array[x] == "GCA" or array[x] == "GCG":
                        result += "Ala"+"-"
                    elif array[x] == "GGU" or array[x] == "GGC" or array[x] == "GGA" or array[x] == "GGG":
                        result += "Gly"+"-"
                    elif array[x] == "GAU" or array[x] == "GAC":
                        result += "Asp"+"-"
                    elif array[x] == "GAA" or array[x] == "GAG":
                        result += "Glu"+"-"
                    else:
                        pass
                final = result[:-1]
                print(final)    
        else:
            print("Something Went Wrong")
    else:
        break
self = input()