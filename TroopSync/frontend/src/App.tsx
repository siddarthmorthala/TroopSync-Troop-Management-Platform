const members = [
  { name: "Aidan Brooks", role: "Scout", patrol: "Raven" },
  { name: "Mrs. Carter", role: "Committee Chair", patrol: "-" },
  { name: "Mr. Nguyen", role: "Treasurer", patrol: "-" },
];

const events = [
  "Lake Ray Roberts Campout",
  "Popcorn Fundraiser Kickoff",
  "PLC Planning Night",
  "Community Service Clean-Up"
];

const badges = [
  "Camping",
  "First Aid",
  "Citizenship in the Community",
  "Personal Management"
];

export default function App() {
  return (
    <div className="container">
      <div className="header">
        <div>
          <div className="brand">TroopSync</div>
          <div className="subtle">Commissioned by Troop 261 leadership • Plano, TX • Modern SaaS troop operations platform</div>
        </div>
        <span className="badge">Scouts BSA</span>
      </div>

      <div className="grid">
        <div className="card"><h3>Members</h3><div style={{fontSize: 32}}>48</div><div className="small">Scouts, parents, and leaders</div></div>
        <div className="card"><h3>Open Events</h3><div style={{fontSize: 32}}>6</div><div className="small">Campouts, fundraisers, meetings</div></div>
        <div className="card"><h3>Service Hours</h3><div style={{fontSize: 32}}>142</div><div className="small">Tracked this quarter</div></div>
        <div className="card"><h3>Advancement Alerts</h3><div style={{fontSize: 32}}>9</div><div className="small">Ready for review or sign-off</div></div>
      </div>

      <div className="list">
        <div className="card">
          <h3>Roster & Roles</h3>
          {members.map((m) => (
            <div className="row" key={m.name}><span>{m.name}</span><span className="small">{m.role} • {m.patrol}</span></div>
          ))}
          <div className="small">Role-based access for scouts, parents, Scoutmaster, ASMs, Treasurer, Advancement Chair, and committee leaders.</div>
        </div>

        <div className="card">
          <h3>Planning & Operations</h3>
          <ul>
            <li>Real-time planning notes and task assignments</li>
            <li>Campout gear checklists and duty rosters</li>
            <li>Carpool coordination with seat counts</li>
            <li>Meal planner with shopping list generation</li>
            <li>Automated event reminders for parents</li>
          </ul>
        </div>

        <div className="card">
          <h3>Advancement & Engagement</h3>
          <div className="row"><span>Rank tracking</span><span className="badge green">Rules Checked</span></div>
          <div className="row"><span>Merit badge guide</span><span className="badge gold">Interactive</span></div>
          <div className="small" style={{marginBottom: 8}}>Popular badges</div>
          <ul>{badges.map((b) => <li key={b}>{b}</li>)}</ul>
          <div className="small">Service hours leaderboard and import-ready advancement workflows included.</div>
        </div>
      </div>

      <div className="card" style={{marginTop: 20}}>
        <h3>Feature Coverage</h3>
        <div className="small">Advancement, roster, events, fundraisers, scout accounts, reminders, imports, service logging, leaderboards, communication, and internal reporting.</div>
      </div>
    </div>
  );
}
