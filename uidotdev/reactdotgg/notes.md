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
