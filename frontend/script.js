document.getElementById("fetchGreeting").addEventListener("click", async () => {
    const response = await fetch("http://127.0.0.1:8000/greet");
    const data = await response.json();
    document.getElementById("greetMessage").innerText = data.message;
});

document.getElementById("fetchFact").addEventListener("click", async () => {
    const response = await fetch("http://127.0.0.1:8000/random-fact");
    const data = await response.json();
    document.getElementById("factMessage").innerText = data.fact;
});

document.getElementById("calcForm").addEventListener("submit", async (event) => {
    event.preventDefault();
    
    const num1 = document.getElementById("num1").value;
    const num2 = document.getElementById("num2").value;
    const operation = document.getElementById("operation").value;

    if (!num1 || !num2) {
        document.getElementById("calcResult").innerText = "Please enter both numbers.";
        return;
    }

    try {
        const response = await fetch(`http://127.0.0.1:8000/calculate?num1=${encodeURIComponent(num1)}&num2=${encodeURIComponent(num2)}&operation=${encodeURIComponent(operation)}`);
        const data = await response.json();

        if (response.ok) {
            document.getElementById("calcResult").innerText = "Result: " + data.result;
        } else {
            document.getElementById("calcResult").innerText = "Error: " + data.error;
        }
    } catch (error) {
        document.getElementById("calcResult").innerText = "Request failed.";
    }
});


document.getElementById("reverseBtn").addEventListener("click", async () => {
    const text = document.getElementById("reverseInput").value;
    const response = await fetch(`http://127.0.0.1:8000/reverse-text?text=${text}`);
    const data = await response.json();
    document.getElementById("reverseOutput").innerText = "Reversed: " + data.reversed;
});

document.getElementById("wordCountBtn").addEventListener("click", async () => {
    const text = document.getElementById("wordCountInput").value;
    const response = await fetch(`http://127.0.0.1:8000/word-count?text=${text}`);
    const data = await response.json();
    document.getElementById("wordCountOutput").innerText = "Word Count: " + data.word_count;
});
