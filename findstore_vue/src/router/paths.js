export default [
  {
    path: "",
    view: "Home",
    name: "home"
  },
  // 유저
  {
    path: "/signup",
    view: "accounts/Signup",
    name: "signup"
  },
  {
    path: "/update",
    view: "accounts/Update",
    name: "update"
  },
  {
    path: "/detail",
    view: "accounts/Detail",
    name: "detail"
  },
  // meeting
  {
    path: "/meeting",
    view: "meeting/MeetingList",
    name: "meetinglist"
  },
  {
    path: "/meeting/:m_id",
    view : "meeting/MeetingDetail",
    name : "meetingDetail"
  },
  // store
  {
    path: "/store",
    view: "stores/StoreDetail",
    name: "storedetail"
  },
  // promise
  {
    path: "/promise",
    view: "promise/MakePromise1",
    name: "promise"
  },
];