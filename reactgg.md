# React.gg course

- declarative is abstraction on top of imperative
- react provides declarative api to describe ui
- treats html/js/css together to describe a view
- view is function of state

- pure functions - functional programming principle

  - consider function as taking input and returning output
  - anything else is side effect - state modifications, external api etc.
  - pure function = no side effects and consistent output
  - testable and readable

- since react components are just functions, the same intution about organizing and when to abstract logic applies
  - single responsibility principle
  - if a component is being reused somewhere else - make it its own file. otherwise just put it in the file where it's being used
- react components are always pure functions - any side effects should be wrapped in event handlers
- "React's rendering process must always be pure"

- react component = function that returns a description of some ui
- to show nothing return `null` or `false`

- react is about composable functions - need a way to pass data in - props
- props are to components what arguments are to functions
- any data passed between the opening and closing tags of a component can be accessed on `props.children`

- react elements = object representation of a dom node
- can create one manually using `react/jsx-runtime`
- components are just functions that optionally accept input via props, and return a React element
- elements are the building blocks of react not components
- `jsx` takes two arguments: 1: tag name string, 2: list of attributes you want the element to have

```
import { jsx } from "react/jsx-runtime"

const element = jsx("h1", {
  className: "header",
  children: "Profile"
})
```

- if react sees a component as the first argument to `jsx` it will recursively render that component as well as all children in order to get all the react elements and the final description of the UI
- using jsx function or using jsx syntax is the same - both creating an element
- react uses object representation of DOM to easily compare an element between renders and avoid updating the whole DOM tree on changes

- "Hooks are functions, but it’s helpful to think of them as unconditional declarations about your component’s needs. You use React features at the top of your component similar to how you import modules at the top of your file." - React docs

- rendering - react calls functions (components) with intention of updating view
- 1. snapshot of component with props, state, event handlers and description of UI (based on props and state)
- 2. takes that description and updates view
- intial render starting at root
- react only re-renders when a component's state changes
- when an event handler is invoked it has access to the props/state as they were in the moment in time when the snapshot was created
- if the event handler contains an invocation of `useState`'s updater function and the state is different then React will trigger a re-render - creating a new snapshot and updating the view
- react only re-renders once every updater function has been taken into account and we're sure what the final state will be
- react calculates state through internal algorithm know as 'batching'
- if multiple invocations of the same updater function are found, it keeps track of all of them but only the result of the last one is used as the new state
- you can use the value of the previous invocation by passing the next invocation a function that will take the value of the previous invocation as an argument
- react only re-renders once per event handler even if that event handler contains updates for multiple pieces of state
- on re-render react will render the component that triggered it and all its children - regardless of whether they accept props
- rendering is rarely a performance issue
- has to re-render child components in case of non-pure components (`useRef`/`useEffect`)
- if there's an expensive component that you only want to re-render when its props change you can use `React.memo`
- `StrictMode` component only runs in dev mode and causes everything to re-render twice to make sure that components are pure

- you can pass a callback to useState that will only set the default on the initial render - lazy loading state

- effects
- components have to be pure but in order to be useful we need to be able to interact with apis, the browser, the DOM etc.
- when a component renders it should do so without running into any side effects
- if a side effect is triggered by an event then it should be put in the event handler
- if a side effect is synchronizing your component with some external system then use `useEffect` - will delay the execution until after the component has rendered
- by default useEffect will run on every render
- can pass in a dependency array to useEffect, then `useEffect` will only run when one of the dependencies change. quality using `Object.is`
- the dependency array is everything that react needs to re-synchronize with the outside system
- if you return a function from `useEffect` React will call it each time before calling `useEffect` again and then one final time when the component is removed from the DOM - can be used to ensure we don't have stale data when network requests are being made

- sometimes you don't to pass state in as a dependency - you can pass the state updater a function that will get the current state as an argument
- with StrictMode components will render and extra time and effects will run an extra time - good way to uncover inconsistencies
- what needs to go in dependency array for an effect? reactive values - any value that can change between renders - props, state or any variables defined within a component

Rule #0
When a component renders, it should do so without running into any side effects

Rule #1
If a side effect is triggered by an event, put that side effect in an event handler

Rule #2
If a side effect is synchronizing your component with some outside system, put that side effect inside useEffect

Rule #3
If a side effect is synchronizing your component with some outside system and that side effect needs to run _before_ the browser paints the screen, put that side effect inside useLayoutEffect

Rule #4
If a side effect is subscribing to an external store, use the useSyncExternalStore hook

- set ignore/stale flag within useEffect to ignore previous requests
- useEffect itself can't be async but can call await

- useRef persists state across renders that is nothing to do with the view. since in react the view is a function of state. e.g. setInterval timer IDs
- useRef creates a value that is preserved across renders but won't rerender when it's changed
- ref.current is mutable just like any other variable
- Whenever you pass a ref as a prop to a React element, React will put a reference to the DOM node it creates into that ref's current property.

## mental model of react summary

In React, your view is a function of your state – both of which you encapsulate inside of a component. To get your application, you compose all of your components together.

To get data down the component tree, you use props. To get data up the component tree, you use callbacks.

Sometimes you need to do things that don't fit into this regular React paradigm, these are called side effects and React provides some escape hatches for these scenarios.

If you have a side effect that is triggered by an event, put it in an event handler. If you have a side effect that is synchronizing your component with some outside system, put it inside of useEffect. If you need to preserve a value across renders, but that value has nothing to do with the view, and therefore, React doesn't need to re-render when it changes, put it in a ref using useRef.

====

- context: passing data without using props
- When you create a new Context, what React gives you is an object with a Provider property.
- Provider accepts a value prop which is the data that you want to teleport to any component in Provider's subtree
- To get access to what was passed to the Provider's value prop, you use React's useContext hook, passing it the Context as the first argument.
- In a way, you can kind of think of using Context as creating "shadow props" – where you're making data available to a component, just without having to explicitly pass it down.
- Context is a teleporter not a manager of state
- The only other question we have left to answer is how does React handle re-rendering when the data we're teleporting changes?
- The answer is satisfyingly simple – React re-renders the same way it always does, when state changes.
- if you call a context without it being in a provider it will take the default value passed on creation

```
import * as React from "react"

const expletive = React.createContext("shit")

function ContextualExclamation() {
  const word = React.useContext(expletive)

  return (
    <span>Oh, {word}!</span>
  )
}

function VisitGrandmasHouse() {
  return (
    <expletive.Provider value="darn">
      <h1>Grandma's House 🏡</h1>
      <ContextualExclamation />
    </expletive.Provider>
  )
}

function VisitFriendsHouse() {
  return (
    <React.Fragment>
      <h1>Friend's House 🏚</h1>
      <ContextualExclamation />
    </React.Fragment>
  )
}

export default function App() {
  return (
    <main>
      <VisitFriendsHouse />
      <VisitGrandmasHouse />
    </main>
  )
}
```

## UseReducer

- think javascript reduce that iterates over an array and returns a single value, and at each step in the array the reducer is passed the current item and the interim state
- useReducer goes over user actions over time, and whenever a new action occurs we can invoke the reducer to get the new 'interim' state
- similar to useState except instead of returning a way of updating the state we return dispatch that when called will invoke the reducer function
- can be used similar to redux - instead of dispatching values we can dispatch 'actions' that are then handled in the reducer
- state management is completely decoupled from the component itself by mapping actions directly to state transitions in the reducer function
- can be used to manage multiple pieces of state as an object, and can pass an object as dispatch argument
- makes it very simple to update one piece of state based on another piece of state - good rule for when to use useReducer

- fundamentally both `useState` and `useReducer` allow you to manage state that is preserved across renders and will trigger a re-render when it changes
- lots of useState calls is fine but an imperative solution - whereas useReducer can be more declarative where you just need to pass an action
- If different pieces of state update independently from one another (hovering, selected, etc.), useState should work fine. If your state tends to be updated together or if updating one piece of state is based on another piece of state, go with useReducer.

## Exercises/code

### State

```
import React from "react";

function PasswordInput({ minimum = 8 }) {
  const [inputValue, setInputValue] = React.useState("");
  const [isInputValueVisible, setIsInputValueVisible] = React.useState(false);
  const [thresholdMet, setThresholdMet] = React.useState(false);

  const handleChange = (e) => {
    setInputValue(e.target.value);
    setThresholdMet(e.target.value.length >= minimum);

  };

  const handleToggleVisibility = () => {
    setIsInputValueVisible(!isInputValueVisible);
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (thresholdMet) {
      alert("Password submitted");
    } else {
      alert("You need a longer password");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="limited-text-input">Password:</label>
        <span className={thresholdMet ? "no-error" : "error"}>
          {inputValue.length}
        </span>
      </div>
      <div>
        <input
          placeholder="Enter a password"
          type={isInputValueVisible ? "text" : "password"}
          id="limited-text-input"
          value={inputValue}
          onChange={handleChange}
        />
        <button type="button" onClick={handleToggleVisibility}>
          {isInputValueVisible ? "🙊" : "🙈"}
        </button>
      </div>

      <button type="submit" className="primary">
        Submit
      </button>
    </form>
  );
}

export default PasswordInput;
```

```
import * as React from "react";

const initialFormData = {
  name: "",
  email: "",
  address: "",
  city: "",
  zipcode: ""
};

export default function MultiStepForm() {
  const [currentStep, setCurrentStep] = React.useState(1);
  const [formData, setFormData] = React.useState(initialFormData);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    })
  };

  const handleNextStep = () => {
    setCurrentStep(currentStep+1);
  };

  const handlePrevStep = () => {
    setCurrentStep(currentStep-1);
  };

  const handleSubmit = () => {
    alert("Thank you for your submission");
    setFormData(initialFormData);
    setCurrentStep(1);
  };

  if (currentStep === 1) {
    return (
      <form onSubmit={handleSubmit}>
        <h2>Personal Information</h2>
        <div>
          <label>Step {currentStep} of 3</label>
          <progress value={currentStep} max={3} />
        </div>
        <div>
          <label htmlFor="name">Name</label>
          <input
            required
            name="name"
            id="name"
            placeholder="Enter your name"
            value={formData.name}
            onChange={handleChange}
          />
        </div>
        <div>
          <label htmlFor="email">Email</label>
          <input
            required
            name="email"
            id="email"
            type="email"
            placeholder="Enter your email"
            value={formData.email}
            onChange={handleChange}
          />
        </div>
        <button type="button" className="secondary" onClick={handleNextStep}>
          Next
        </button>
      </form>
    );
  } else if (currentStep === 2) {
    return (
      <form onSubmit={handleSubmit}>
        <h2>Address</h2>
        <div>
          <label>Step {currentStep} of 3</label>
          <progress value={currentStep} max={3} />
        </div>
        <div>
          <label htmlFor="address">Address</label>
          <input
            required
            name="address"
            id="address"
            type="address"
            placeholder="What is your address?"
            value={formData.address}
            onChange={handleChange}
          />
        </div>
        <div>
          <label htmlFor="city">City</label>
          <input
            required
            name="city"
            id="city"
            placeholder="What city do you live in?"
            value={formData.city}
            onChange={handleChange}
          />
        </div>
        <div>
          <label htmlFor="zipcode">Zipcode</label>
          <input
            required
            name="zipcode"
            id="zipcode"
            type="number"
            placeholder="What is your zipcode?"
            value={formData.zipcode}
            onChange={handleChange}
          />
        </div>
        <div>
          <button className="secondary" type="button" onClick={handleNextStep}>
            Next
          </button>
          <button type="button" className="link" onClick={handlePrevStep}>
            Previous
          </button>
        </div>
      </form>
    );
  } else if (currentStep === 3) {
    return (
      <form onSubmit={handleSubmit}>
        <h2>Confirm your information:</h2>
        <div>
          <label>Step {currentStep} of 3</label>
          <progress value={currentStep} max={3} />
        </div>
        <table>
          <tbody>
            {Object.keys(formData).map((key) => {
              return (
                <tr key={key}>
                  <td>{key}</td>
                  <td>{formData[key]}</td>
                </tr>
              );
            })}
          </tbody>
        </table>
        <div>
          <button className="primary" type="submit">
            Submit
          </button>
          <button type="button" className="link" onClick={handlePrevStep}>
            Previous
          </button>
        </div>
      </form>
    );
  } else {
    return null;
  }
}

```

```
import * as React from "react";

export default function FormBuilder() {
  const [formFields, setFormFields] = React.useState([]);

  const handleAddFormField = (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);

    const newField = {
      id: new Date().getTime(),
      type: formData.get("type"),
      label: formData.get("label"),
      placeholder: formData.get("placeholder"),
      required: formData.get("required"),
      value: "",
    };

    setFormFields([...formFields, newField]);
  };

  const handleUpdateFormField = (id, updatedField) => {
    setFormFields(
      formFields.map((f) => (f.id === id ? { ...f, ...updatedField } : f))
    );
  };

  const handleDeleteFormField = (id) => {
    setFormFields(formFields.filter((f) => f.id !== id));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    alert(JSON.stringify(formFields, null, 2));
  };

  return (
    <div>
      <h1>Form Builder</h1>
      <form id="form-builder" onSubmit={handleAddFormField}>
        <fieldset>
          <legend>Add a field</legend>
          <label htmlFor="type">Field Type</label>
          <select name="type" id="type">
            <option value="text">Text</option>
            <option value="number">Number</option>
            <option value="email">Email</option>
            <option value="password">Password</option>
          </select>
          <div>
            <label htmlFor="required">Required</label>
            <input type="checkbox" name="required" id="required" />
          </div>
          <label htmlFor="label">Label</label>
          <input
            required
            type="text"
            name="label"
            id="label"
            placeholder="Enter a label"
          />
          <label htmlFor="placeholder">Placeholder</label>
          <input
            required
            type="text"
            id="placeholder"
            name="placeholder"
            placeholder="Enter a placeholder"
          />
          <button type="submit" className="secondary">
            Add Form Field
          </button>
        </fieldset>
      </form>
      <form id="form-fields" onSubmit={handleSubmit}>
        <fieldset>
          <legend>Form Fields</legend>
          <ul>
            {formFields.map((field) => (
              <li key={field.id}>
                <label htmlFor={`input-${field.id}`}>{field.label}</label>
                <input
                  id={`input-${field.id}`}
                  required={field.required}
                  placeholder={field.placeholder}
                  type={field.type}
                  value={field.value}
                  onChange={(e) =>
                    handleUpdateFormField(field.id, { value: e.target.value })
                  }
                />
                <button
                  type="button"
                  className="secondary"
                  onClick={() => handleDeleteFormField(field.id)}
                >
                  Delete
                </button>
              </li>
            ))}
          </ul>
          <span>Your form fields will show here</span>
          <button className="primary">Submit</button>
        </fieldset>
      </form>
    </div>
  );
}

```

### Effects

```
import * as React from "react";

const items = [
  "Apple",
  "Banana",
  "Cherry",
  "Date",
  "Fig",
  "Grape",
  "Honeydew",
  "Lemon",
  "Mango",
  "Nectarine",
  "Orange",
  "Papaya",
  "Raspberry",
  "Strawberry",
  "Watermelon"
];

export default function SearchFilter() {
  const [searchTerm, setSearchTerm] = React.useState("");
  const filteredItems = items.filter(i => i.toLowerCase().includes(searchTerm.toLowerCase()))

  return (
    <div>
      <h1>Search Filter</h1>
      <input
        type="text"
        placeholder="Search..."
        value={searchTerm}
        onChange={e=>setSearchTerm(e.target.value)}
      />
      <ul>
        {filteredItems.map((item) => (
          <li key={item}>{item}</li>
        ))}
      </ul>
    </div>
  );
}

```

```
import * as React from "react";

export default function Clock() {
  const [time, setTime] = React.useState(null);

  React.useEffect(() => {
    const t = setInterval(() => setTime(new Date()), 1000);

    return () => clearInterval(t);
  },[]);

  if (time === null) return null;

  return (
    <section>
      <h1>Current Time</h1>
      <p>{time.toLocaleTimeString()}</p>
    </section>
  );
}

```

```
import * as React from "react";

export default function CountryInfo() {
  const [countryCode, setCountryCode] = React.useState("AU");
  const [data, setData] = React.useState(null);
  const [isLoading, setIsLoading] = React.useState(true);
  const [error, setError] = React.useState(null);

  const handleChange = (e) => {
    setCountryCode(e.target.value);
  };

  React.useEffect(() => {
    const fetchCountry = async () => {
      setIsLoading(true);
      setError(null);
      let stale = false;
      const url = `https://restcountries.com/v2/alpha/${countryCode}`;

      try {
        const response = await fetch(url);
        const data = await response.json();
        if (!stale) {
          setData(data);
        }
      } catch (error) {
        if (!stale) {
          setData(null);
          setError(error);
        }
      } finally {
        if (!stale) {
          setIsLoading(false);
        }
      }
    };

    fetchCountry();

    return () => {
      stale = true;
    };
  }, [countryCode]);

  return (
    <section>
      <header>
        <h1>Country Info:</h1>

        <label htmlFor="country">Select a country:</label>
        <div>
          <select id="country" value={countryCode} onChange={handleChange}>
            <option value="AU">Australia</option>
            <option value="CA">Canada</option>
            <option value="CN">China</option>
            <option value="FR">France</option>
            <option value="DE">Germany</option>
            <option value="IN">India</option>
            <option value="JP">Japan</option>
            <option value="MX">Mexico</option>
            <option value="GB">United Kingdom</option>
            <option value="US">United States of America</option>
          </select>
          {isLoading && <span>Loading...</span>}
          {error && <span>{error.message}</span>}
        </div>
      </header>

      {data && (
        <article>
          <h2>{data.name}</h2>
          <table>
            <tbody>
              <tr>
                <td>Capital:</td>
                <td>{data.capital}</td>
              </tr>
              <tr>
                <td>Region:</td>
                <td>{data.region}</td>
              </tr>
              <tr>
                <td>Population:</td>
                <td>{data.population}</td>
              </tr>
              <tr>
                <td>Area:</td>
                <td>{data.area}</td>
              </tr>
            </tbody>
          </table>
        </article>
      )}
    </section>
  );
}

```

```
import * as React from "react";
import { RotatingLines } from "react-loader-spinner";

const fetchData = async ({ query = "", page = 0, tag = "" }) => {
  return fetch(
    `https://hn.algolia.com/api/v1/search?query=${query}&tags=${encodeURIComponent(
      tag
    )}&page=${page}`
  )
    .then((response) => response.json())
    .then((json) => ({
      results: json.hits || [],
      pages: json.nbPages || 0,
      resultsPerPage: json.hitsPerPage || 20,
    }));
};

export default function HackerNewsSearch() {
  const [query, setQuery] = React.useState("");
  const [results, setResults] = React.useState([]);
  const [tag, setTag] = React.useState("story");
  const [page, setPage] = React.useState(0);
  const [resultsPerPage, setResultsPerPage] = React.useState(0);
  const [totalPages, setTotalPages] = React.useState(50);
  const [loading, setLoading] = React.useState(false);

  React.useEffect(() => {
    let stale = false;
    const handleFetchData = async () => {
      setLoading(true);
      setResults([]);

      const results = await fetchData({query, page, tag});

      if (stale) return;

      setResults(results.results);
      setResultsPerPage(results.resultsPerPage);
      setTotalPages(results.pages);

      setLoading(false);
    };
    handleFetchData();

    return () => {
      stale = true;
    };
  }, [query, page, tag]);

  const handleSearch = (e) => {
    setQuery(e.target.value);
    setPage(0);
  };

  const handleTag = (e) => {
    setTag(e.target.value);
    setPage(0);
  };

  const handleNextPage = () => {
    setPage(page + 1);
  };

  const handlePrevPage = () => {
    setPage(page - 1);
  };

  return (
    <main>
      <h1>Hacker News Search</h1>
      <form onSubmit={(e) => e.preventDefault()}>
        <div>
          <label htmlFor="query">Search</label>
          <input
            type="text"
            id="query"
            name="query"
            value={query}
            onChange={handleSearch}
            placeholder="Search Hacker News..."
          />
        </div>
        <div>
          <label htmlFor="tag">Tag</label>
          <select id="tag" name="tag" onChange={handleTag} value={tag}>
            <option value="story">Story</option>
            <option value="ask_hn">Ask HN</option>
            <option value="show_hn">Show HN</option>
            <option value="poll">Poll</option>
          </select>
        </div>
      </form>
      <section>
        <header>
          <h2>
            <span>
              {totalPages === 0
                ? "No Results"
                : `Page ${page + 1} of ${totalPages}`}
            </span>
            <RotatingLines
              strokeColor="grey"
              strokeWidth="5"
              animationDuration="0.75"
              width="20"
              visible={loading}
            />
          </h2>
          <div>
            <button
              className="link"
              onClick={handlePrevPage}
              disabled={page <= 0}
            >
              Previous
            </button>
            <button
              className="link"
              onClick={handleNextPage}
              disabled={page + 1 >= totalPages}
            >
              Next
            </button>
          </div>
        </header>
        <ul>
          {results.map(({ url, objectID, title }, index) => {
            const href =
              url || `https://news.ycombinator.com/item?id=${objectID}`;
            const position = resultsPerPage * page + index + 1;

            return (
              <li key={objectID}>
                <span>{position}.</span>
                <a href={href} target="_blank" rel="noreferrer">
                  {title}
                </a>
              </li>
            );
          })}
        </ul>
      </section>
    </main>
  );
}

```

### Ref

```
import * as React from "react";

function TextInput() {
  const inputRef = React.useRef(null);

  React.useEffect(() => {
    if (inputRef.current) {
      inputRef.current.focus();
    }
  }, []);

  return (
    <div>
      <h1>Autofocus Input</h1>
      <label htmlFor="focus">Email Address</label>
      <input
        ref={inputRef}
        id="focus"
        type="email"
        placeholder="Enter your email"
      />
    </div>
  );
}

export default TextInput;
```

```
import * as React from "react";

export default function VideoPlayer() {
  const [isPlaying, setIsPlaying] = React.useState(false);
  const videoRef = React.useRef(null);

  const handleTogglePlay = () => {
    isPlaying ? videoRef.current.pause() : videoRef.current.play();
    setIsPlaying(!isPlaying);
  };

  return (
    <section className="container">
      <h1>Video Player</h1>
      <article>
        <video ref={videoRef} poster="https://image.mux.com/TbVCJiOghmISJgg4AznPfFHYRfiVoek8OJHF56Y01oR4/thumbnail.webp">
          <source
            src="https://stream.mux.com/TbVCJiOghmISJgg4AznPfFHYRfiVoek8OJHF56Y01oR4/high.mp4"
            type="video/mp4"
          />
        </video>
        <div>
          <button
            title={isPlaying ? "Pause" : "Play"}
            onClick={handleTogglePlay}
          >
            {isPlaying ? "⏸" : "▶"}
          </button>
        </div>
      </article>
    </section>
  );
}

```

```
import * as React from "react";

export default function FieldNotes() {
  const [notes, setNotes] = React.useState([
    "Components encapsulate both the visual representation of a particular piece of UI as well as the state and logic that goes along with it.",
    "The same intuition you have about creating and composing together functions can directly apply to creating and composing components. However, instead of composing functions together to get some value, you can compose components together to get some UI.",
    "JSX combines the power and expressiveness of JavaScript with the readability and accessibility of HTML",
    "Just like a component enabled the composition and reusability of UI, hooks enabled the composition and reusability of non-visual logic.",
  ]);

  const lastNoteRef = React.useRef(null);

  React.useEffect(() => {
    if (lastNoteRef.current) {
      lastNoteRef.current.scrollIntoView();
    }
  });

  const handleSubmit = (e) => {
    e.preventDefault();
    const form = e.target;
    const formData = new FormData(form);
    const newNote = formData.get("note");
    if (!newNote.trim()) return;

    setNotes([...notes, newNote]);
    form.reset();
  };

  return (
    <article>
      <h1>Field Notes</h1>
      <div>
        <ul>
          {notes.map((msg, index) => (
            <li
              ref={index === notes.length - 1 ? lastNoteRef : null}
              key={index}
            >
              {msg}
            </li>
          ))}
        </ul>
        <form onSubmit={handleSubmit}>
          <input
            required
            type="text"
            name="note"
            placeholder="Type your note..."
          />
          <button className="link" type="submit">
            Submit
          </button>
        </form>
      </div>
    </article>
  );
}
```

```
import * as React from "react";
import { closeIcon } from "./icons";

export default function ClickOutside() {
  const [isOpen, setIsOpen] = React.useState(false);
  const ref = React.useRef(null);

  React.useEffect(() => {
    const handlePointerDown = (e) => {
      if (ref.current && !ref.current.contains(e.target)) {
        setIsOpen(false);
      }
    }
    document.addEventListener("pointerdown", handlePointerDown);

    return () => {
      document.removeEventListener("pointerdown", handlePointerDown)
    }
  })

  const handleOpenModal = () => {
    if (isOpen === false) {
      setIsOpen(true);
    }
  };

  const handleCloseModal = () => {
    setIsOpen(false);
  };

  return (
    <>
      <section>
        <h1>Click Outside</h1>
        <button className="link" onClick={handleOpenModal}>
          Open Modal
        </button>
      </section>
      {isOpen && (
        <dialog ref={ref}>
          <button onClick={handleCloseModal}>{closeIcon}</button>
          <h2>Modal</h2>
          <p>
            Click outside the modal to close (or use the button) whatever you
            prefer.
          </p>
        </dialog>
      )}
    </>
  );
}

```

```
import * as React from "react";

export default function ExpandingTextarea() {
  const [text, setText] = React.useState("");
  const ref = React.useRef(null);

  const handleChange = (e) => {
    setText(e.target.value);
    ref.current.style.height = "inherit";
    ref.current.style.height = ref.current.scrollHeight + "px";
  }

  return (
    <section className="container">
      <h1>Expanding Textarea</h1>
      <label htmlFor="textarea">Enter or paste in some text</label>
      <textarea
        ref={ref}
        id="textarea"
        placeholder="Enter some text"
        value={text}
        onChange={handleChange}
        rows={1}
      />
    </section>
  );
}

```

```
import * as React from "react";

export default function FollowTheLeader() {
  const [position, setPosition] = React.useState([0, 0]);
  const ref = React.useRef(null);

  React.useEffect(() => {
    document.addEventListener("click", handleClick);

    return () => {
      document.addEventListener("click", handleClick);
    };
  }, []);

  const handleClick = ({ clientX, clientY }) => {
    const {width, height} = ref.current.getBoundingClientRect();

    setPosition([clientX - width/2, clientY - height/2]);
  };

  return (
    <div className="wrapper">
      <div
        ref={ref}
        className="box"
        style={{
          transform: `translate(${position[0]}px, ${position[1]}px)`,
          transition: "transform 1s",
        }}
      />
    </div>
  );
}

```

### Context

```
import * as React from "react";
import Dashboard from "./Dashboard";

const authContext = React.createContext({
  isAuthenticated: false,
  login: () => {},
  logout: () => {}
});

const AuthProvider = ({ children }) => {
  const isAuthenticated = false;

  const login = () => {};

  const logout = () => {};

  return <authContext.Provider>{children}</authContext.Provider>;
};

function NavBar() {
  const logout = () => {};
  const isAuthenticated = false;

  return (
    <nav>
      <span role="img" aria-label="Money bags emoji">
        💰
      </span>
      {isAuthenticated && (
        <button className="link" onClick={logout}>
          Logout
        </button>
      )}
    </nav>
  );
}

function LoginForm() {
  const login = () => {};

  const handleSubmit = (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    const username = formData.get("username");
    const password = formData.get("password");
    login(username, password);
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Log In</h2>
      <div>
        <label htmlFor="username">Username:</label>
        <input
          required
          type="text"
          id="username"
          name="username"
          placeholder="Enter your username"
        />
      </div>
      <div>
        <label htmlFor="password">Password:</label>
        <input
          required
          id="password"
          type="password"
          name="password"
          placeholder="Enter your password"
        />
      </div>
      <button className="primary" type="submit">
        Login
      </button>
    </form>
  );
}

function Main() {
  const isAuthenticated = false;

  return <main>{isAuthenticated ? <Dashboard /> : <LoginForm />}</main>;
}

export default function App() {
  return (
    <AuthProvider>
      <NavBar />
      <Main />
    </AuthProvider>
  );
}

```

```
import * as React from "react";

const translations = {
  en: {
    hello: "Hello!",
    welcome: "Welcome to our app!",
  },
  es: {
    hello: "¡Hola!",
    welcome: "¡Bienvenido a nuestra aplicación!",
  },
  fr: {
    hello: "Bonjour !",
    welcome: "Bienvenue dans notre application !",
  },
  de: {
    hello: "Hallo!",
    welcome: "Willkommen in unserer App!",
  },
};

const languageContext = React.createContext({
  language: "en",
  changeLanguage: () => {},
  translation: (key) => key,
});

function LanguageProvider({ children }) {
  const [language, setLanguage] = React.useState("en");

  const changeLanguage = (newLanguage) => {
    setLanguage(newLanguage);
  };

  const translation = (key) => {
    return translations[language][key];
  };

  return (
    <languageContext.Provider value={{ language, changeLanguage, translation }}>
      {children}
    </languageContext.Provider>
  );
}

function LanguageSwitcher() {
  const { language, changeLanguage } = React.useContext(languageContext);

  return (
    <div>
      <select value={language} onChange={(e) => changeLanguage(e.target.value)}>
        <option value="en">English</option>
        <option value="es">Español</option>
        <option value="fr">Français</option>
        <option value="de">Deutsch</option>
      </select>
    </div>
  );
}

function Greeting() {
  const { translation } = React.useContext(languageContext);

  return (
    <div>
      <h1>{translation("hello")}</h1>
      <p>{translation("welcome")}</p>
    </div>
  );
}

export default function App() {
  return (
    <LanguageProvider>
      <LanguageSwitcher />
      <Greeting />
    </LanguageProvider>
  );
}

```

```
import * as React from "react";

const tabContext = React.createContext({
  activeTabValue: null,
  setActiveTabValue: () => {},
});

function TabProvider({ children, defaultValue }) {
  const [activeTabValue, setActiveTabValue] = React.useState(defaultValue);

  return (
    <tabContext.Provider value={{ activeTabValue, setActiveTabValue }}>
      {children}
    </tabContext.Provider>
  );
}

function TabTrigger({ value, children }) {
  const { activeTabValue, setActiveTabValue } = React.useContext(tabContext);

  const handleSetActiveTabValue = () => {
    setActiveTabValue(value);
  };

  return (
    <button
      onClick={handleSetActiveTabValue}
      className={`tab ${activeTabValue === value ? "active" : ""}`}
    >
      {children}
    </button>
  );
}

function TabContent({ value, children }) {
  const { activeTabValue } = React.useContext(tabContext);

  if (activeTabValue !== value) {
    return null;
  }

  return children;
}

export default function App() {
  return (
    <section>
      <h1>Tabs</h1>
      <TabProvider defaultValue="tab-1">
        <div className="tabs">
          <TabTrigger value="tab-1">Tab 1</TabTrigger>
          <TabTrigger value="tab-2">Tab 2</TabTrigger>
          <TabTrigger value="tab-3">Tab 3</TabTrigger>
        </div>
        <TabContent value="tab-1">Tab Content 1</TabContent>
        <TabContent value="tab-2">Tab Content 2</TabContent>
        <TabContent value="tab-3">Tab Content 3</TabContent>
      </TabProvider>
    </section>
  );
}

```

```
import * as React from "react";

const videoPlaybackContext = React.createContext({
  playingVideoId: null,
  setPlayingVideoId: () => {},
});

function VideoPlaybackProvider({ children }) {
  const [playingVideoId, setPlayingVideoId] = React.useState(null);

  return (
    <videoPlaybackContext.Provider
      value={{ playingVideoId, setPlayingVideoId }}
    >
      {children}
    </videoPlaybackContext.Provider>
  );
}

function VideoItem({ videoId, title, poster, src }) {
  const { playingVideoId, setPlayingVideoId } =
    React.useContext(videoPlaybackContext);
  const videoRef = React.useRef(null);

  const videoIsActive = playingVideoId === videoId;

  React.useEffect(() => {
    if (videoIsActive) {
      videoRef.current.play();
    } else {
      videoRef.current.pause();
    }
  }, [videoIsActive]);

  const handleTogglePlay = () => {
    videoIsActive ? setPlayingVideoId(null) : setPlayingVideoId(videoId);
  };

  return (
    <li>
      <h3>{title}</h3>
      <article>
        <video ref={videoRef} poster={poster}>
          <source src={src} type="video/mp4" />
        </video>
        <button
          title={videoIsActive ? "Pause" : "Play"}
          onClick={handleTogglePlay}
        >
          {videoIsActive ? "⏸" : "▶"}
        </button>
      </article>
    </li>
  );
}

function NewsFeed() {
  const videos = [
    {
      id: 1,
      title: "The React Way",
      poster: "https://react.gg/img/visualized-og2.jpg",
      src: "https://stream.mux.com/TbVCJiOghmISJgg4AznPfFHYRfiVoek8OJHF56Y01oR4/high.mp4",
    },
    {
      id: 2,
      title: "The History of the Web",
      poster: "https://react.gg/img/visualized-og1.jpg",
      src: "https://stream.mux.com/EwJPlEBa0046jGSVdYOnRsX9WnqHjytgIBXwkOt7LvVg/high.mp4",
    },
    {
      id: 3,
      title: "Rendering, Visualized",
      poster: "https://react.gg/img/visualized-og5.jpg",
      src: "https://stream.mux.com/VvQKMwPEOq5BUnc9eRN4sL5sUEZrHqWxNlCbpXSkE3I/high.mp4",
    },
  ];

  return (
    <div>
      <h1>News Feed</h1>
      <ul>
        {videos.map((video) => (
          <VideoItem
            key={video.id}
            videoId={video.id}
            title={video.title}
            poster={video.poster}
            src={video.src}
          />
        ))}
      </ul>
    </div>
  );
}

export default function App() {
  return (
    <VideoPlaybackProvider>
      <NewsFeed />
    </VideoPlaybackProvider>
  );
}

```

### UseReducer

```
import * as React from "react";

const initialFormData = {
  name: "",
  email: "",
  address: "",
  city: "",
  zipcode: ""
};

const reducer = (state, action) => {
  switch (action.type) {
      case "next_step":
        return {
          ...state,
          currentStep: state.currentStep+1,
        }
      case "prev_step":
        return {
          ...state,
          currentStep: state.currentStep-1
        }
      case "change":
        return {
          ...state,
          formData: {...state.formData, [action.name]: [action.value]}
        }
      case "reset":
        return {
          currentStep: 1,
          formData: initialFormData
        }
  }
};

export default function MultistepFormReducer() {
  const [{currentStep, formData}, dispatch] = React.useReducer(reducer, {currentStep: 1, formData: initialFormData});

  const handleNextStep = () => {
    dispatch({type:"next_step"})
  };

  const handlePrevStep = () => {
    dispatch({type:"prev_step"})
  };

  const handleChange = (e) => {
    const {name, value} = e.target;
    dispatch({type:"change", name, value})
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    alert("Thank you for your submission");
    dispatch({type:"reset"})
  };

  if (currentStep === 1) {
    return (
      <form onSubmit={handleSubmit}>
        <h2>Personal Information</h2>
        <div>
          <label>Step {currentStep} of 3</label>
          <progress value={currentStep} max={3} />
        </div>
        <div>
          <label htmlFor="name">Name</label>
          <input
            required
            name="name"
            id="name"
            placeholder="Enter your name"
            value={formData.name}
            onChange={handleChange}
          />
        </div>
        <div>
          <label htmlFor="email">Email</label>
          <input
            required
            name="email"
            id="email"
            type="email"
            placeholder="Enter your email"
            value={formData.email}
            onChange={handleChange}
          />
        </div>
        <button type="button" className="secondary" onClick={handleNextStep}>
          Next
        </button>
      </form>
    );
  } else if (currentStep === 2) {
    return (
      <form onSubmit={handleSubmit}>
        <h2>Address</h2>
        <div>
          <label>Step {currentStep} of 3</label>
          <progress value={currentStep} max={3} />
        </div>
        <div>
          <label htmlFor="address">Address</label>
          <input
            required
            name="address"
            id="address"
            type="address"
            placeholder="What is your address?"
            value={formData.address}
            onChange={handleChange}
          />
        </div>
        <div>
          <label htmlFor="city">City</label>
          <input
            required
            name="city"
            id="city"
            placeholder="What city do you live in?"
            value={formData.city}
            onChange={handleChange}
          />
        </div>
        <div>
          <label htmlFor="zipcode">Zipcode</label>
          <input
            required
            name="zipcode"
            id="zipcode"
            type="number"
            placeholder="What is your zipcode?"
            value={formData.zipcode}
            onChange={handleChange}
          />
        </div>
        <div>
          <button className="secondary" type="button" onClick={handleNextStep}>
            Next
          </button>
          <button type="button" className="link" onClick={handlePrevStep}>
            Previous
          </button>
        </div>
      </form>
    );
  } else if (currentStep === 3) {
    return (
      <form onSubmit={handleSubmit}>
        <h2>Confirm your information:</h2>
        <div>
          <label>Step {currentStep} of 3</label>
          <progress value={currentStep} max={3} />
        </div>
        <table>
          <tbody>
            {Object.keys(formData).map((key) => {
              return (
                <tr key={key}>
                  <td>{key}</td>
                  <td>{formData[key]}</td>
                </tr>
              );
            })}
          </tbody>
        </table>
        <div>
          <button className="primary" type="submit">
            Submit
          </button>
          <button type="button" className="link" onClick={handlePrevStep}>
            Previous
          </button>
        </div>
      </form>
    );
  } else {
    return null;
  }
}

```

```
import * as React from "react";
import { createTask } from "./utils";

function reducer(tasks, action) {
  switch (action.type) {
    case "add":
      return [...tasks, action.task];
    case "update":
      return tasks.map((task) =>
        task.id === action.id
          ? {
              ...task,
              status: task.status === "pending" ? "completed" : "pending",
            }
          : task
      );
    case "delete":
      return tasks.filter((task) => task.id !== action.id);
    default:
      throw new Error("unsupported action type");
  }
  return tasks;
}

export default function TaskManager() {
  const [tasks, dispatch] = React.useReducer(reducer, []);

  const handleUpdateTaskStatus = (id) => {
    dispatch({ type: "update", id });
  };

  const handleDeleteTask = (id) => {
    dispatch({ type: "delete", id });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    const formData = new FormData(e.target);
    dispatch({ type: "add", task: createTask(formData.get("task")) });

    e.target.reset();
  };

  return (
    <div>
      <h1>Task Manager</h1>
      <form onSubmit={handleSubmit}>
        <input name="task" placeholder="Task title" />
        <button className="primary" type="submit">
          Add Task
        </button>
      </form>
      <ul>
        {tasks.map((task) => (
          <li key={task.id}>
            <div>
              <button
                className={`status ${task.status}`}
                onClick={() => handleUpdateTaskStatus(task.id)}
              />
              {task.title}
            </div>
            <button className="link" onClick={() => handleDeleteTask(task.id)}>
              Delete
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

```

```
import * as React from "react";

const products = [
  { id: 1, name: "Poké Ball", price: 10 },
  { id: 2, name: "Great Ball", price: 20 },
  { id: 3, name: "Ultra Ball", price: 30 }
];

function calculateTotal(cart) {
  return cart.reduce((total, product) => {
    return total + product.quantity * product.price;
  }, 0);
}

const initialState = [];

function reducer(cart, action) {
  if (action.type === "add") {
    const inCart = Boolean(cart.find((item) => item.id === action.id));

    if (!inCart) {
      const product = products.find((p) => p.id === action.id);
      return [...cart, { ...product, quantity: 1 }];
    }

    return cart.map((item) =>
      item.id === action.id ? { ...item, quantity: item.quantity + 1 } : item
    );
  } else if (action.type === "update") {
    if (action.adjustment === "increment") {
      return cart.map((item) =>
        item.id === action.id ? { ...item, quantity: item.quantity + 1 } : item
      );
    }

    const item = cart.find(({ id }) => action.id === id);

    if (item.quantity === 1) {
      return cart.filter((item) => item.id !== action.id);
    } else {
      return cart.map((item) =>
        item.id === action.id ? { ...item, quantity: item.quantity - 1 } : item
      );
    }
  } else {
    throw new Error("This action type isn't supported.")
  }
}

export default function ShoppingCart() {
  const [cart, dispatch] = React.useReducer(reducer, initialState);

  const handleAddToCart = (id) => dispatch({ type: "add", id });

  const handleUpdateQuantity = (id, adjustment) => {
    dispatch({
      type: "update",
      id,
      adjustment
    });
  };

  return (
    <main>
      <h1>Poké Mart</h1>
      <section>
        <div>
          <ul className="products">
            {products.map((product) => (
              <li key={product.id}>
                {product.name} - ${product.price}
                <button
                  className="primary"
                  onClick={() => handleAddToCart(product.id)}
                >
                  Add to cart
                </button>
              </li>
            ))}
          </ul>
        </div>
      </section>
      <hr />
      <aside>
        <div>
          <h2>Shopping Cart</h2>
          <ul>
            {cart.map((item) => (
              <li key={item.id}>
                {item.name}
                <div>
                  <button
                    onClick={() =>
                      handleUpdateQuantity(item.id, "decrement")
                    }
                  >
                    -
                  </button>
                  {item.quantity}
                  <button
                    onClick={() =>
                      handleUpdateQuantity(item.id, "increment")
                    }
                  >
                    +
                  </button>
                </div>
              </li>
            ))}
            {!cart.length && <li>Cart is empty</li>}
          </ul>
        </div>
        <hr />

        <h3>Total: ${calculateTotal(cart)}</h3>
      </aside>
    </main>
  );
}
```

```
import * as React from "react";

const initialState = {
  past: [],
  present: 0,
  future: [],
};

function reducer(state, action) {
  const { past, present, future } = state;

  switch (action) {
    case "increment":
      return {
        past: [...past, present],
        present: present + 1,
        future: [],
      };
    case "decrement":
      return {
        past: [...past, present],
        present: present - 1,
        future: [],
      };
    case "undo":
      return {
        past: past.slice(0, -1),
        present: past.at(-1),
        future: [present, ...future],
      };
    case "redo":
      return {
        past: [...past, present],
        present: future[0],
        future: future.slice(1),
      };
    default:
      throw new Error("unsupported action")
  }

  return state;
}

export default function CounterWithUndoRedo() {
  const [state, dispatch] = React.useReducer(reducer, initialState);

  const handleIncrement = () => {
    dispatch("increment");
  };
  const handleDecrement = () => {
    dispatch("decrement");
  };
  const handleUndo = () => {
    dispatch("undo");
  };
  const handleRedo = () => {
    dispatch("redo");
  };

  return (
    <div>
      <h1>Counter: {state.present}</h1>
      <button className="link" onClick={handleIncrement}>
        Increment
      </button>
      <button className="link" onClick={handleDecrement}>
        Decrement
      </button>
      <button
        className="link"
        onClick={handleUndo}
        disabled={!state.past.length}
      >
        Undo
      </button>
      <button
        className="link"
        onClick={handleRedo}
        disabled={!state.future.length}
      >
        Redo
      </button>
    </div>
  );
}
```
