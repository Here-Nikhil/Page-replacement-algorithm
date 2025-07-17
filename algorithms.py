def fifo(reference_string, frame_size):
    """First In, First Out page replacement algorithm.
    Args:
        reference_string (list): List of page numbers.
        frame_size (int): Number of frames available.
    Returns:
        dict: Contains total page faults and step-by-step details.
    """
    frames = []
    page_faults = 0
    steps = []

    for page in reference_string:
        current_state = frames.copy()
        fault = False

        if page not in frames:
            fault = True
            if len(frames) < frame_size:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)
            page_faults += 1

        steps.append({
            "page": page,
            "frames_before": current_state,
            "frames_after": frames.copy(),
            "page_fault": fault
        })

    return {"faults": page_faults, "steps": steps}

def lru(reference_string, frame_size):
    """Least Recently Used page replacement algorithm.
    Args:
        reference_string (list): List of page numbers.
        frame_size (int): Number of frames available.
    Returns:
        dict: Contains total page faults and step-by-step details.
    """
    frames = []
    page_faults = 0
    steps = []

    for page in reference_string:
        current_state = frames.copy()
        fault = False

        if page not in frames:
            fault = True
            if len(frames) < frame_size:
                frames.append(page)
            else:
                frames.pop(0)  # Remove least recently used (oldest)
                frames.append(page)
            page_faults += 1
        else:
            frames.remove(page)  # Move to end (most recently used)
            frames.append(page)

        steps.append({
            "page": page,
            "frames_before": current_state,
            "frames_after": frames.copy(),
            "page_fault": fault
        })

    return {"faults": page_faults, "steps": steps}

def optimal(reference_string, frame_size):
    """Optimal page replacement algorithm (replaces page needed furthest in future).
    Args:
        reference_string (list): List of page numbers.
        frame_size (int): Number of frames available.
    Returns:
        dict: Contains total page faults and step-by-step details.
    """
    frames = []
    page_faults = 0
    steps = []

    for i, page in enumerate(reference_string):
        current_state = frames.copy()
        fault = False

        if page not in frames:
            fault = True
            if len(frames) < frame_size:
                frames.append(page)
            else:
                future = reference_string[i+1:]
                replace = None
                max_dist = -1
                for frame in frames:
                    try:
                        dist = future.index(frame)
                    except ValueError:
                        dist = float('inf')
                    if dist > max_dist:
                        max_dist = dist
                        replace = frame
                frames[frames.index(replace)] = page
            page_faults += 1

        steps.append({
            "page": page,
            "frames_before": current_state,
            "frames_after": frames.copy(),
            "page_fault": fault
        })

    return {"faults": page_faults, "steps": steps}

def second_chance(reference_string, frame_size):
    """Second Chance page replacement algorithm (uses reference bits).
    Args:
        reference_string (list): List of page numbers.
        frame_size (int): Number of frames available.
    Returns:
        dict: Contains total page faults and step-by-step details.
    """
    frames = []
    ref_bits = []
    pointer = 0
    page_faults = 0
    steps = []

    for page in reference_string:
        current_state = frames.copy()
        fault = False

        if page not in frames:
            fault = True
            if len(frames) < frame_size:
                frames.append(page)
                ref_bits.append(1)
            else:
                while ref_bits[pointer]:
                    ref_bits[pointer] = 0
                    pointer = (pointer + 1) % frame_size
                frames[pointer] = page
                ref_bits[pointer] = 1
                pointer = (pointer + 1) % frame_size
            page_faults += 1
        else:
            ref_bits[frames.index(page)] = 1

        steps.append({
            "page": page,
            "frames_before": current_state,
            "frames_after": frames.copy(),
            "page_fault": fault
        })

    return {"faults": page_faults, "steps": steps}

def clock(reference_string, frame_size):
    """Clock page replacement algorithm (circular list with pointer).
    Args:
        reference_string (list): List of page numbers.
        frame_size (int): Number of frames available.
    Returns:
        dict: Contains total page faults and step-by-step details.
    """
    frames = []
    ref_bits = []
    pointer = 0
    page_faults = 0
    steps = []

    for page in reference_string:
        current_state = frames.copy()
        fault = False

        if page not in frames:
            fault = True
            if len(frames) < frame_size:
                frames.append(page)
                ref_bits.append(1)
            else:
                while ref_bits[pointer]:
                    ref_bits[pointer] = 0
                    pointer = (pointer + 1) % len(frames)
                frames[pointer] = page
                ref_bits[pointer] = 1
                pointer = (pointer + 1) % len(frames)
            page_faults += 1
        else:
            ref_bits[frames.index(page)] = 1

        steps.append({
            "page": page,
            "frames_before": current_state,
            "frames_after": frames.copy(),
            "page_fault": fault
        })

    return {"faults": page_faults, "steps": steps}

# Dictionary for extensible algorithm registration
ALGORITHMS = {
    "FIFO": fifo,
    "LRU": lru,
    "Optimal": optimal,
    "Second Chance": second_chance,
    "Clock": clock
}

if __name__ == "__main__":
    """Test the algorithms with a sample input."""
    ref_string = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    frame_size = 3
    for algo_name, algo_func in ALGORITHMS.items():
        result = algo_func(ref_string, frame_size)
        print(f"{algo_name}: {result['faults']} faults")