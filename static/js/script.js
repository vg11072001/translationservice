async function translateText() {
    const text = document.getElementById('text').value;
    const target_language = document.getElementById('target_language').value;

    try {
        let translatedTextElement = document.getElementById('translated-text');
        let splitInfoElement = document.getElementById('split-info');

        if (text.length > 1000) {
            const chunks = [];
            for (let i = 0; i < text.length; i += 1000) {
                chunks.push(text.substring(i, i + 1000));
            }

            const translatedChunks = [];
            for (const chunk of chunks) {
                const response = await fetch(`/api/translate?text=${encodeURIComponent(chunk)}&target_language=${target_language}`, {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json'
                    }
                });

                if (!response.ok) {
                    throw new Error('Failed to translate text');
                }

                const data = await response.json();
                translatedChunks.push(data.translated_text);
            }

            const translatedText = translatedChunks.join('\n');
            translatedTextElement.innerText = `Translated Text (split into ${chunks.length} parts):\n${translatedText}`;
            splitInfoElement.innerText = `Note: The text was split into ${chunks.length} parts for translation.`;
        } else {
            const response = await fetch(`/api/translate?text=${encodeURIComponent(text)}&target_language=${target_language}`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                }
            });

            if (!response.ok) {
                throw new Error('Failed to translate text');
            }

            const data = await response.json();
            translatedTextElement.innerText = `Translated Text: ${data.translated_text}`;
            splitInfoElement.innerText = '';
        }

        document.getElementById('original-text').innerText = `Original Text: ${text}`;
    } catch (error) {
        alert('Failed to translate text. Please check the server and try again.');
        console.error('Error:', error);
    }
}