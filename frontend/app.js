document.getElementById("load").addEventListener("click", async () => {
  const response = await fetch("http://localhost:8000/insights");
  const data = await response.json();

  const list = document.getElementById("insightList");
  list.innerHTML = "";

  data.forEach(item => {
    const li = document.createElement("li");
    li.textContent = `${item.hero}: ${item.insight}`;
    list.appendChild(li);
  });
});
