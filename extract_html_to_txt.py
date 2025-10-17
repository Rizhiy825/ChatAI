import os
from bs4 import BeautifulSoup
from pathlib import Path

def extract_html_content(html_file_path):
    """
    Extract content from HTML file based on headers and content-text.
    Returns a list of dictionaries with headers and content.
    """
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    results = []
    
    # Find all content divs
    content_divs = soup.find_all('div', class_='content')
    
    for div in content_divs:
        # Find all headers in the current context
        headers = []
        
        # Get h1 (should be at the top level)
        h1 = soup.find('h1')
        if h1 and h1.get_text(strip=True):
            headers.append(h1.get_text(strip=True))
        
        # Find h2 in content-header or directly in content
        h2_in_header = div.find('div', class_='content-header')
        if h2_in_header:
            h2 = h2_in_header.find('h2')
            if h2 and h2.get_text(strip=True):
                headers.append(h2.get_text(strip=True))
        else:
            # Look for h2 directly in div
            h2 = div.find('h2')
            if h2 and h2.get_text(strip=True):
                headers.append(h2.get_text(strip=True))
        
        # Find h3 if exists
        h3 = div.find('h3')
        if h3 and h3.get_text(strip=True):
            headers.append(h3.get_text(strip=True))
        
        # Extract content-text
        content_text_divs = div.find_all('div', class_='content-text')
        if not content_text_divs:
            # Also check for direct paragraphs
            content_text_divs = div.find_all('p')
        
        content_text = ""
        for content_div in content_text_divs:
            text = content_div.get_text(separator='\n', strip=True)
            if text:
                content_text += text + "\n\n"
        
        # Also check for content-list
        content_list_divs = div.find_all('div', class_='content-list')
        for content_div in content_list_divs:
            text = content_div.get_text(separator='\n', strip=True)
            if text:
                content_text += text + "\n\n"
        
        # Also check for content-text2
        content_text2_divs = div.find_all('div', class_='content-text2')
        for content_div in content_text2_divs:
            text = content_div.get_text(separator='\n', strip=True)
            if text:
                content_text += text + "\n\n"
        
        # Only add if we have headers and content
        if headers and content_text.strip():
            results.append({
                'headers': headers,
                'content': content_text.strip()
            })
    
    return results

def process_all_html_files(input_folder, output_folder):
    """
    Process all HTML files in the input folder and create TXT files in the output folder.
    """
    # Create output folder if it doesn't exist
    Path(output_folder).mkdir(parents=True, exist_ok=True)
    
    # Get all HTML files
    html_files = [f for f in os.listdir(input_folder) if f.endswith('.html')]
    
    print(f"Found {len(html_files)} HTML files to process")
    
    for html_file in html_files:
        html_path = os.path.join(input_folder, html_file)
        print(f"\nProcessing: {html_file}")
        
        try:
            # Extract content
            content_items = extract_html_content(html_path)
            
            if not content_items:
                print(f"  No content found in {html_file}")
                continue
            
            print(f"  Found {len(content_items)} content sections")
            
            # Create TXT files
            for item in content_items:
                headers = item['headers']
                content = item['content']
                
                # Create filename from headers
                filename = '.'.join(headers) + '.txt'
                # Clean filename from invalid characters
                filename = filename.replace('/', '-').replace('\\', '-').replace(':', '-')
                filename = filename.replace('?', '').replace('*', '').replace('"', '')
                filename = filename.replace('<', '').replace('>', '').replace('|', '')
                
                output_path = os.path.join(output_folder, filename)
                
                # Write content to file
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print(f"  Created: {filename}")
        
        except Exception as e:
            print(f"  Error processing {html_file}: {str(e)}")
    
    print(f"\n✓ Processing complete! Files saved to: {output_folder}")

if __name__ == "__main__":
    input_folder = r"c:\projects\ChatAI\InputData"
    output_folder = r"c:\projects\ChatAI\Files"
    
    process_all_html_files(input_folder, output_folder)
