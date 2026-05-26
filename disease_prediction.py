print("=== AI Healthcare Disease Prediction System ===")

name = input("Enter patient name: ")
age = input("Enter patient age: ")
symptom = input("Enter your symptom: ")

print("\nAnalyzing symptoms...\n")

if symptom.lower() == "fever":
    print("Possible Disease: Viral Infection")

elif symptom.lower() == "cough":
    print("Possible Disease: Common Cold")

elif symptom.lower() == "headache":
    print("Possible Disease: Migraine")

elif symptom.lower() == "chest pain":
    print("Possible Disease: Heart-related issue")

else:
    print("Please consult a doctor for proper diagnosis.")

print("\nThank you for using AI Healthcare System.")