import { HelmetProvider } from "react-helmet-async";
import { createBrowserRouter, Outlet, RouterProvider } from "react-router-dom";

function Root() {
  return (
    <div className="app-container">
      <main>
        <Outlet />
      </main>
    </div>
  );
}

const browserRouter = createBrowserRouter([
  {
    path: "/",
    element: <Root />,
    errorElement: <div>Some Error Occured</div>,
    children: [
      {
        path: "login",
        element: <div>Login Page</div>,
      },
    ],
  },
]);

export default function Router() {
  return (
    <HelmetProvider>
      <RouterProvider
        router={browserRouter}
        fallbackElement={<div>Falling back...</div>}
      />
    </HelmetProvider>
  );
}
