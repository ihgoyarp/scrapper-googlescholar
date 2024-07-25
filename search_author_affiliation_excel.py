import pandas as pd
from scholarly import scholarly

def search_author_by_name_and_affiliation(author_name, affiliation):
    # Mencari penulis berdasarkan nama
    search_query = scholarly.search_author(author_name)
    
    # Filter hasil pencarian berdasarkan afiliasi
    for author in search_query:
        author = scholarly.fill(author)
        if affiliation.lower() in author['affiliation'].lower():
            print(f"Author: {author['name']}")
            print(f"Affiliation: {author['affiliation']}")
            print(f"Total Citations: {author['citedby']}")
            print(f"Publications:")
            print("-" * 80)
            
            # Mengumpulkan data publikasi
            publications_data = []
            for idx, pub in enumerate(author['publications'][:100], start=1):  # Batasi hasil ke 10 publikasi pertama
                pub = scholarly.fill(pub)
                title = pub['bib']['title']
                url = pub.get('pub_url', 'No URL available')
                accreditation = "N/A"  # Replace with actual accreditation if available
                year = pub['bib'].get('pub_year', 'No year available')
                pub_type = pub['bib'].get('type', 'No type available')
                
                publications_data.append([idx, title, url, accreditation, year, pub_type])
                
                # Print to console (optional)
                print(f"No: {idx}")
                print(f"Title: {title}")
                print(f"URL: {url}")
                print(f"Accreditation: {accreditation}")
                print(f"Year: {year}")
                print(f"Type: {pub_type}")
                print("-" * 80)
            
            # Membuat DataFrame dari data publikasi
            df = pd.DataFrame(publications_data, columns=["No", "Judul", "URL / Alamat", "Akreditasi", "Tahun", "Jenis"])
            
            # Menyimpan DataFrame ke file Excel
            file_name = f"{author['name']}_publications.xlsx"
            df.to_excel(file_name, index=False)
            
            print(f"Data saved to {file_name}")
            return
    
    print("Author not found with the given affiliation.")

if __name__ == "__main__":
    author_name = input("Masukkan nama penulis: ")
    affiliation = input("Masukkan afiliasi penulis: ")
    search_author_by_name_and_affiliation(author_name, affiliation)
