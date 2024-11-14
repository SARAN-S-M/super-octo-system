class BayesTheorem:
    def __init__(self, disease_name, P_D, P_T_given_D, P_T_given_not_D):
        self.disease_name = disease_name
        self.P_D = P_D
        self.P_T_given_D = P_T_given_D
        self.P_T_given_not_D = P_T_given_not_D

    def calculate_posterior(self):
        """Calculate the posterior probability using Bayes' Theorem."""
        P_not_D = 1 - self.P_D
        P_T = (self.P_T_given_D * self.P_D) + (self.P_T_given_not_D * P_not_D)
        P_D_given_T = (self.P_T_given_D * self.P_D) / P_T
        return P_D_given_T

    def validate_probabilities(self):
        """Validate that all probabilities are between 0 and 1."""
        if not (0 <= self.P_D <= 1 and 0 <= self.P_T_given_D <= 1 and 0 <= self.P_T_given_not_D <= 1):
            raise ValueError("All probabilities should be between 0 and 1.")

    def display_result(self):
        """Display the result of the Bayes' Theorem calculation."""
        try:
            self.validate_probabilities()
            posterior_probability = self.calculate_posterior()
            print(f"The probability of having {self.disease_name} given a positive test result is {posterior_probability:.2%}")
        except ValueError as e:
            print(f"Invalid input: {e}")

if __name__ == "__main__":
    try:
        disease_name = input("Enter the name of the disease: ")

        P_D = float(input(f"Enter the prior probability of having {disease_name} (as a decimal, e.g., 0.01 for 1%): "))
        P_T_given_D = float(input(f"Enter the sensitivity of the test for {disease_name} (as a decimal, e.g., 0.90 for 90%): "))
        P_T_given_not_D = float(input(f"Enter the false positive rate of the test for {disease_name} (as a decimal, e.g., 0.05 for 5%): "))

        bayes = BayesTheorem(disease_name, P_D, P_T_given_D, P_T_given_not_D)
        bayes.display_result()

    except ValueError as e:
        print(f"Invalid input: {e}")
