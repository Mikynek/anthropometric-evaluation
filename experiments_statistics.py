from helpers.generate_latex_table import generate_latex_table_mediapipe

def print_analysis_statistics(max_differences):
    print("SUMMARY")
    print("Max differences:")
    for key, max_diff in max_differences.items():
        print(f"  {key}: {max_diff.count} occurrences, average distance difference: {max_diff.value / max_diff.count}")

    if max_differences:
        # Finding which proportion differs the most
        most_differing_proportion = max(max_differences, key=lambda k: max_differences[k].count)
        print(f"The most differing proportion: {most_differing_proportion} with {max_differences[most_differing_proportion].count} occurrences.")
        # Calculate the average distance difference for the most differing proportion
        average_distance_difference = max_differences[most_differing_proportion].value / max_differences[most_differing_proportion].count
        print(f"Average distance difference for the most differing proportion: {average_distance_difference}")
    else:
        print("No differences found.")

    latex_table = generate_latex_table_mediapipe(max_differences)
    # print(latex_table)
    
def print_verification_statistics_deepface(verification_results, distances):
    success_count = verification_results.count(True)
    failure_count = verification_results.count(False)
    total_pairs = len(verification_results)
    average_distance = sum(distances) / len(distances)

    print("\nVerification Statistics:")
    print(f"Total Pairs: {total_pairs}")
    print(f"Successful Verifications: {success_count}")
    print(f"Failed Verifications: {failure_count}")
    print(f"Average Distance: {average_distance:.6f}")

    if total_pairs > 0:
        success_rate = (success_count / total_pairs) * 100
        print(f"Success Rate: {success_rate:.2f}%")
    else:
        print("No pairs to verify.")