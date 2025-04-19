# made by itslouizz on github
# this is my third tiny project, I know that there are other much better options and its just for learning a bit of python. and i used a bit of deepseek cause i am tl dumb to solve problems with f strings myself lol

import textwrap

def get_yes_no_input(prompt):
    while True:
        response = input(f"{prompt} (y/n): ").strip().lower()
        if response in ('y', 'yes'):
            return True
        elif response in ('n', 'no'):
            return False
        print("Please answer with y/n or yes/no")

def get_user_input(field_name, is_multiline=False):
    if is_multiline:
        print(f"\n{field_name} (Press Enter twice to finish):")
        lines = []
        while True:
            line = input()
            if not line:
                if lines and not lines[-1]:
                    break
            lines.append(line)
        return "\n".join(filter(None, lines))
    return input(f"\n{field_name}: ").strip()

def select_theme():
    themes = {
        '1': 'Classic',
        '2': 'Minimal',
        '3': 'Fancy'
    }
    print("\nSelect a theme for your profile:")
    for num, theme in themes.items():
        print(f"{num}. {theme}")
    while True:
        choice = input("Enter choice (1-3): ")
        if choice in themes:
            return themes[choice]
        print("Invalid choice. Please select 1-3")

def add_external_links():
    links = {}
    print("\n=== External Links ===")
    link_types = {
        '1': ('YouTube Channel', False),
        '2': ('PayPal (Donations)', False),
        '3': ('Personal Blog', False),
        '4': ('Other Link', True)
    }
    
    while get_yes_no_input("Would you like to add an external link?"):
        print("\nAvailable link types:")
        for num, (link_name, _) in link_types.items():
            print(f"{num}. {link_name}")
        
        choice = input("Select link type (1-4): ")
        if choice not in link_types:
            print("Invalid choice. Please try again.")
            continue
            
        link_name, needs_description = link_types[choice]
        if needs_description:
            description = input("Link description: ").strip()
            url = input("URL: ").strip()
            links[description] = url
        else:
            url = input(f"{link_name} URL: ").strip()
            links[link_name] = url
    
    return links if links else None

def format_profile(profile, theme, external_links=None):
    formatted = []
    if theme == 'Classic':
        formatted.append("="*50)
        formatted.append("YOUR DEVELOPER PROFILE".center(50))
        formatted.append("="*50)
        for section, content in profile.items():
            formatted.append(f"\n{section.upper()}:\n")
            wrapped = textwrap.fill(content, width=70) if '\n' not in content else content
            formatted.append(wrapped)
    elif theme == 'Minimal':
        for section, content in profile.items():
            cleaned_content = content.replace('\n', ' | ')
            formatted.append(f"{section}: {cleaned_content}")
    else:  # Fancy
        formatted.append("╔" + "═"*48 + "╗")
        formatted.append("║" + "✨ DEVELOPER PROFILE ✨".center(48) + "║")
        formatted.append("╚" + "═"*48 + "╝")
        for section, content in profile.items():
            formatted.append(f"\n★ {section.upper()} ★")
            wrapped = textwrap.fill(content, width=70) if '\n' not in content else content
            formatted.append(wrapped)
    
    if external_links:
        if theme == 'Classic':
            formatted.append("\n\nEXTERNAL LINKS:\n")
        elif theme == 'Minimal':
            formatted.append("\nExternal Links: ")
        else:  # Fancy
            formatted.append("\n\n🔗 EXTERNAL LINKS 🔗\n")
        
        for desc, url in external_links.items():
            if theme == 'Minimal':
                formatted.append(f"{desc}: {url}")
            else:
                formatted.append(f"{desc}: {url}\n")
    
    return '\n'.join(formatted)

def save_to_file(content):
    if not get_yes_no_input("Save profile to file?"):
        return
    filename = input("Enter filename (default: developer_profile.txt): ") or "developer_profile.txt"
    if not (filename.endswith('.txt') or filename.endswith('.md')):
        filename += '.txt'
    try:
        with open(filename, 'w') as f:
            f.write(content)
        print(f"\033[92mProfile saved successfully to {filename}!\033[0m")
    except Exception as e:
        print(f"\033[91mError saving file: {e}\033[0m")

def create_programmer_profile():
    print("\n" + "="*50)
    print("PROGRAMMER PROFILE GENERATOR".center(50))
    print("="*50)
    
    profile = {}
    fields = [
        ('Full Name', False),
        ('Professional Title', False),
        ('Years of Coding Experience', False),
        ('Technical Skills', True),
        ('Favorite Programming Languages', True),
        ('Areas of Expertise', True),
        ('Projects & Experience', True),
        ('Development Tools', False),
        ('GitHub/Portfolio Link', False),
        ('Favorite Programming Quote', True),
        ('Career Status', False),
        ('Motivation for Programming', True),
        ('Learning Goals', True)
    ]
    
    for field, is_multiline in fields:
        if get_yes_no_input(f"Add {field} to your profile?"):
            profile[field] = get_user_input(field, is_multiline)
    
    external_links = add_external_links()
    theme = select_theme()
    profile_content = format_profile(profile, theme, external_links)
    
    print("\n" + "="*50)
    print(profile_content)
    print("\n\033[92mProfile generated successfully!\033[0m 🎉")
    
    save_to_file(profile_content)

if __name__ == "__main__":
    create_programmer_profile()