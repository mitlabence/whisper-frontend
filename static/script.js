let mediaRecorder;
let audioChunks = [];

document.getElementById("record").onclick = async () => {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    mediaRecorder = new MediaRecorder(stream);
    audioChunks = [];

    mediaRecorder.ondataavailable = e => audioChunks.push(e.data);

    mediaRecorder.onstop = async () => {
        const blob = new Blob(audioChunks, { type: 'audio/webm' });
        const formData = new FormData();
        formData.append('audio_data', blob, 'recording.webm');

        document.getElementById("status").innerText = "Uploading...";

        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();
        document.getElementById("status").innerText = "Server response: " + result.transcription_response;
    };

    mediaRecorder.start();
    document.getElementById("record").disabled = true;
    document.getElementById("stop").disabled = false;
    document.getElementById("status").innerText = "Recording...";
};

document.getElementById("stop").onclick = () => {
    mediaRecorder.stop();
    document.getElementById("record").disabled = false;
    document.getElementById("stop").disabled = true;
    document.getElementById("status").innerText = "Processing...";
};
