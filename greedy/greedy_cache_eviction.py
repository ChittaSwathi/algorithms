# time complexity O(n.k)
"""The Optimal Offline Caching (Belady’s Algorithm) is fundamentally based on knowing future requests in advance, 
which means that in practice, it requires scanning future requests to determine which page to evict. 
This theoretical algorithm is already optimal in terms of minimizing page faults, but it’s not efficient in practice 
due to the lookahead mechanism"""
#if done in LRU cache -- time complexity would reduce to O(1)

from collections import defaultdict

def optimal_caching(pages, cache_size):
    cache = set()  # Use a set for fast cache lookup
    page_positions = defaultdict(list)  # Stores future positions of each page
    page_faults = 0  # to count cache misses

    # Precompute the future positions of each page
    for i, page in enumerate(pages):
        page_positions[page].append(i)

    for i, page in enumerate(pages):
        # Remove the current request from future positions
        page_positions[page].pop(0)

        # If page is already in cache, no page fault
        if page in cache:
            print(f"Page {page} already in cache: {list(cache)}")
            continue

        # Cache miss
        page_faults += 1

        # If cache has space, add page
        if len(cache) < cache_size:
            cache.add(page)
            print(f"Page {page} added to cache: {list(cache)}")
        else:
            # Cache is full, find the optimal page to replace
            farthest = -1
            page_to_evict = None

            # For each page in cache, find when it will be used next
            for cached_page in cache:
                if not page_positions[cached_page]:  # If not used again, evict it
                    page_to_evict = cached_page
                    break
                else:
                    next_use = page_positions[cached_page][0]
                    if next_use > farthest:
                        farthest = next_use
                        page_to_evict = cached_page

            # Evict the farthest used page and add the new page to the cache
            print(f"Page {page_to_evict} evicted from cache")
            cache.remove(page_to_evict)
            cache.add(page)
            print(f"Page {page} added to cache: {list(cache)}")

    return page_faults

# Example usage
if __name__ == "__main__":
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    cache_size = 3

    page_faults = optimal_caching(pages, cache_size)
    print(f"\nTotal page faults: {page_faults}")
