class Preference:

    def __init__(self, preferences: dict):
        """
        Initializing the values and preference dictionay which has
        both voters and their preferences of the candidates. and
        getting the unique candidates list.
        """
        self.preferences = preferences
        self.candidates_list = list(self.get_unique_candidates(preferences))

    def get_unique_candidates(self, preferences: dict):
        """
        Getting the unique candidates list
        """
        unique_list = set()
        for i in preferences.values():
            for canditate in i:
                unique_list.add(canditate)
        return unique_list

    def candidates(self):
        """
        Getting/Returning the candidates list
        """
        return self.candidates_list

    def voters(self):
        """
        Returning the voters lists.
        """
        return list(self.preferences.keys())

    def get_preference(self, canditate, voter):
        """
        Returning the preference value/index of the
        canditate in the respected voter list.
        """
        if voter not in self.preferences or canditate not in self.preferences[voter]:
            raise ValueError("Invalid canditate.")
        return self.preferences[voter].index(canditate)


def dictatorship(preferences: Preference, agent):
    """
    return of the function should be the winner according 
    to the Dictatorship rule described above. 
    If the integer given does not represent a valid 
    agent then a ValueError should be raised.
    """
    # return best_candidate
    if agent not in preferences.voters():
        raise ValueError("Invalid agent selected.")

    # Get the preference list of the agent
    agent_preferences = preferences.preferences[agent]

    # The first candidate in the preference list is the dictator's choice
    return agent_preferences[0]


def scoring_rule(preferences: Preference, score_vector, tie_break):
    """
    function should contain error-handling code for the case when the length of the scoring vector is not 
    n, in that case, a ValueError with a suitable message.
    """
    candidates = preferences.candidates()
    voters = preferences.voters()

    if len(score_vector) != len(candidates):
        raise ValueError("Score vector length does not match number of candidates.")

    # Initialize scores
    scores = {candidate: 0 for candidate in candidates}

    # Assign scores based on preference rankings
    for voter in voters:
        for candidate in candidates:
            rank = preferences.get_preference(candidate, voter)
            scores[candidate] += score_vector[rank]

    # Find the candidates with the highest score
    max_score = max(scores.values())
    winners = [candidate for candidate in candidates if scores[candidate] == max_score]

    # Sort winners based on tie-breaker preference
    winners.sort(key=lambda c: preferences.get_preference(c, tie_break))

    return winners[0]  # Return the best-ranked candidate based on tie-break


def veto(preferences: Preference, tie_break):
    """
    The function should return the winner of the Plurality
    rule as described above, using the tie-breaking option to
    distinguish between possible winners.
    """
    num_candidates = len(preferences.candidates())
    score_vector = [1] * (num_candidates - 1) + [0]
    return scoring_rule(preferences, score_vector, tie_break)


def borda(preferences: Preference, tie_break):
    """
    The function should return the winner of the Borda rule as described above,
    using the tie-breaking option to distinguish between possible winners.
    """
    num_candidates = len(preferences.candidates())
    score_vector = list(range(num_candidates - 1, -1, -1))
    return scoring_rule(preferences, score_vector, tie_break)


def plurality(preferences: Preference, tie_break):
    """
    The function should return the winner of the Veto rule as 
    described above, using the tie-breaking option to 
    distinguish between possible winners.
    """
    num_candidates = len(preferences.candidates())
    score_vector = [1] + [0] * (num_candidates - 1)
    return scoring_rule(preferences, score_vector, tie_break)


def STV(preferences: Preference, tie_break):
    """
    The function should return the winner of the Single Transferable Vote
    rule as described above, using the tie-breaking option to distinguish
    between possible winners.
    """
    candidates = set(preferences.candidates())
    voters = preferences.voters()

    while len(candidates) > 1:
        first_choice_counts = {c: 0 for c in candidates}

        # Count first-choice votes
        for voter in voters:
            for candidate in candidates:
                if preferences.get_preference(candidate, voter) == min(
                    preferences.get_preference(c, voter) for c in candidates
                ):
                    first_choice_counts[candidate] += 1
                    break

        # Remove candidate(s) with the least votes
        min_votes = min(first_choice_counts.values())
        candidates -= {c for c in candidates if first_choice_counts[c] == min_votes}

        if len(candidates) == 0:
            break

    return min(candidates, key=lambda c: preferences.get_preference(c, tie_break))


if __name__ == "__main__":
    d = Preference({
                1: ['A', 'C', 'B', 'D'],
                2: ['A', 'B', 'D', 'C'],
                3: ['C', 'B', 'A', 'D'],
                4: ['B', 'A', 'D', 'C']
            })
    # print(d.candidates())
    # print(d.voters())
    # print(d.get_preference('C', 1))
    # print(Voting.dictatorship(d, 1))