import csv
from scholarly import scholarly

def search_author_publications(author_name):
    # Mencari penulis berdasarkan nama
    search_query = scholarly.search_author(author_name)
    
    # Mengambil penulis pertama dalam hasil pencarian
    author = next(search_query, None)
    
    if author:
        # Mengambil informasi detail penulis
        author = scholarly.fill(author)
        print(f"Author: {author['name']}")
        print(f"Affiliation: {author['affiliation']}")
        print(f"Total Citations: {author['citedby']}")
        print(f"Publications:")
        print("-" * 80)
        
        # Membuka file CSV untuk menulis hasil
        with open(f"{author['name']}_publications.csv", mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Menulis header CSV
            writer.writerow(["Title", "Authors", "Abstract", "URL"])
            
            # Menulis publikasi penulis ke file CSV
            for pub in author['publications'][:10]:  # Batasi hasil ke 10 publikasi pertama
                pub = scholarly.fill(pub)
                title = pub['bib']['title']
                authors = pub['bib']['author']
                abstract = pub['bib'].get('abstract', 'No abstract available')
                url = pub.get('pub_url', 'No URL available')
                writer.writerow([title, authors, abstract, url])
                # Print to console (optional)
                print(f"Title: {title}")
                print(f"Authors: {authors}")
                print(f"Abstract: {abstract}")
                print(f"URL: {url}")
                print("-" * 80)
                
        print(f"Data saved to {author['name']}_publications.csv")
    else:
        print("Author not found.")

if __name__ == "__main__":
    author_name = input("Masukkan nama penulis: ")
    search_author_publications(author_name)
