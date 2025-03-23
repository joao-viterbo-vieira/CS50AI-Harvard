import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(link for link in pages[filename] if link in pages)

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    proba = {}

    for k in corpus:
        proba[k] = 0

    n_pages = len(corpus)

    if corpus[page]:
        links = corpus[page]

    else:
        links = corpus.keys()

    n_links = len(links)

    for page in proba:
        proba[page] = (1 - damping_factor) / n_pages

        if page in links:
            proba[page] += damping_factor / n_links

    return proba


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    rank_pages = {}

    for page in corpus:
        rank_pages[page] = 0

    page = random.choice(list(corpus.keys()))

    for i in range(n):
        rank_pages[page] += 1
        model = transition_model(corpus, page, damping_factor)

        pages = list(model.keys())

        probas = list(model.values())
        page = random.choices(pages, probas)[0]

    final_rank = {page: rank / n for page, rank in rank_pages.items()}

    return final_rank


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    n_pages = len(corpus)

    pagerank = {}

    for page in corpus:
        pagerank[page] = 1 / n_pages

    limit = 0.001

    new_pagerank = pagerank.copy()

    while True:
        for page in corpus:
            total = (1 - damping_factor) / n_pages

            for ex_page in corpus:
                if page in corpus[ex_page]:
                    total += damping_factor * pagerank[ex_page] / len(corpus[ex_page])

                if not corpus[ex_page]:
                    total += damping_factor * pagerank[ex_page] / n_pages
            new_pagerank[page] = total

        converged = True
        for ex_page in pagerank:
            if abs(new_pagerank[ex_page] - pagerank[ex_page]) >= limit:
                converged = False
                break

        if converged:
            break
        else:
            pagerank = new_pagerank.copy()

    return pagerank


if __name__ == "__main__":
    main()
