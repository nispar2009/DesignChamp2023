dismissCookie = () => {
    document.getElementById("cookie").style.display = "none"
    document.getElementById("effect").style.display = "none"
}

answer = (quotes, categs) => {
    const question = (getInput("ask"))
    const key = getInput("filter")
    let ans = []

    if (key == "by") {
        quotes.map(item => {
            if ((item.person).toUpperCase() == question.toUpperCase()) {
                ans.push(item)
            }
        })
    }
    if (key == "about") {
        quotes.map(item => {
            if ((item.categ == categs[question.toUpperCase()]) | (item.quote.includes(question))) {
                ans.push(item)
            }
        })
    }
    if (key == "all") { ans = quotes }

    return ans
}

render = (quotes, categs) => {
    const list = answer(quotes, categs)

    cnt = "<ol>"
    for (const iterator of list) { cnt += `<li>${iterator.quote} &mdash; ${iterator.person}</li>` }
    cnt += "</ol>"

    setValue("ans", cnt)

    if (list.length == 0) { setValue("ans", "We're sorry, there are no quotes which match your selection.") }
}

ux = () => {
    const key = getInput("filter")
    const ask = document.getElementById("ask")

    if (key == "by") {
        ask.placeholder = "Who said it?"
        ask.style.display = "inline"
    }
    if (key == "about") {
        ask.placeholder = "What is it about?"
        ask.style.display = "inline"
    }
    if (key == "all") {
        ask.style.display = "none"
        ask.placeholder = "Everything"
    }

}

toggle = what => {
    document.getElementById(`${what}`).classList.toggle("active")
    document.getElementById(`change-${what}`).classList.toggle("active")
}