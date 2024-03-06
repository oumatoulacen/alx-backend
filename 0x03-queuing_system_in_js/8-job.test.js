import kue from "kue";
import createPushNotificationsJobs from "./8-job.js";
import { assert, expect } from "chai";
import sinon from "sinon";
const queue = kue.createQueue();

const jobs = ["gaslight", "gatekeep", "girlboss"];
let JB;
describe("for createPushNotificationsJobs", () => {
  before(() => queue.testMode.enter());
  after(() => queue.testMode.exit());
  beforeEach(() => (JB = sinon.spy(console, "log")));
  afterEach(() => {
    queue.testMode.clear();
    JB.restore();
  });

  it("should throw error if jobs is not an array", () => {
    assert.throws(
      () => createPushNotificationsJobs(jobs[0], queue),
      Error,
      "Jobs is not an array"
    );
  });

  it("should create", () => {
    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).to.equal(3);
    for (const [idx, job] of Object.entries(queue.testMode.jobs)) {
      expect(job.type).to.equal("push_notification_code_3");
      expect(job.data).to.equal(jobs[idx]);
      expect(console.log.calledWith(`Notification job created: ${job.id}`)).to.be.true;
    }
  });

  it("should progresse", () => {
    createPushNotificationsJobs(jobs, queue);
    let perc = 20;
    for (const job of queue.testMode.jobs) {
      job.emit("progress", perc, 100);
      expect(
        console.log.calledWith(`Notification job ${job.id} ${perc}% complete`)
      ).to.be.true;
      perc *= 2;
    }
  });

  it("should fail", () => {
    createPushNotificationsJobs(jobs, queue);
    const failure = ["Luke", "Chewbacca", "Obi-Wan"];
    for (const [idx, job] of Object.entries(queue.testMode.jobs)) {
      job.emit("failed", new Error(`${failure[idx]}, I am your father!`));
      expect(
        console.log.calledWith(
          `Notification job ${job.id} failed: Error: ${failure[idx]}, I am your father!`
        )
      ).to.be.true;
    }
  });

  it("should complete", () => {
    createPushNotificationsJobs(jobs, queue);
    for (const job of queue.testMode.jobs) {
      job.emit("complete");
      expect(console.log.calledWith(`Notification job ${job.id} completed`)).to
        .be.true;
    }
  });
});
