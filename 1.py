s = "Optimization can occur at a number of levels. Typically the higher levels have greater impact, and are harder to change later on in a project, requiring significant changes or a complete rewrite if they need to be changed. Thus optimization can typically proceed via refinement from higher to lower, with initial gains being larger and achieved with less work, and later gains being smaller and requiring more work. However, in some cases overall performance depends on performance of very low-level portions of a program, and small changes at a late stage or early consideration of low-level details can have outsized impact. Typically some consideration is given to efficiency throughout a project – though this varies significantly – but major optimization is often considered a refinement to be done late, if ever. On longer-running projects there are typically cycles of optimization, where improving one area reveals limitations in another, and these are typically curtailed when performance is acceptable or gains become too small or costly.At the highest level, the design may be optimized to make best use of the available resources, given goals, constraints, and expected use/load. The architectural design of a system overwhelmingly affects its performance. For example, a system that is network latency-bound (where network latency is the main constraint on overall performance) would be optimized to minimize network trips, ideally making a single request (or no requests, as in a push protocol) rather than multiple roundtrips. Choice of design depends on the goals: when designing a compiler, if fast compilation is the key priority, a one-pass compiler is faster than a multi-pass compiler (assuming same work), but if speed of output code is the goal, a slower multi-pass compiler fulfills the goal better, even though it takes longer itself. Choice of platform and programming language occur at this level, and changing them frequently requires a complete rewrite, though a modular system may allow rewrite of only some component – for example, a Python program may rewrite performance-critical sections in C. In a distributed system, choice of architecture (client-server, peer-to-peer, etc.) occurs at the design level, and may be difficult to change, particularly if all components cannot be replaced in sync (e.g., old clients)."


def countelement(s):
    s.replace(".", "")
    s.replace("-", "")
    s.replace(",", "")
    s.replace("!", "")
    s.replace("?", "")
    s.replace(":", "")
    s.replace(";", "")
    s.replace("(", "")
    s.replace(")", "")
    text = s.split()
    result = []
    for i in range(len(text)):
        if text.count(text[i]) >= 10:
            result.append(text[i])

    l2 = []
    for i in range(len(result)):
        if result[i] not in l2:
            l2.append(result[i])
    return print("Повторяющиеся 10 и более раз:", *l2)


def countwords(s):
    s.replace(".", "")
    s.replace("-", "")
    s.replace(",", "")
    s.replace("!", "")
    s.replace("?", "")
    s.replace(":", "")
    s.replace(";", "")
    s.replace("(", "")
    s.replace(")", "")
    text = s.split()
    count = 0
    for i in range(len(text)):
        count += 1
    return print("Количество слов в строке: ", count)


countwords(s)
countelement(s)
